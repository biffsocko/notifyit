#!/bin/env python3
import os
import types
import pytest

pyinotify = pytest.importorskip("pyinotify")   # skips everywhere pyinotify isn't installed
import notifyit


def test_handler_prints_path(capsys):
    event = types.SimpleNamespace(pathname="/tmp/checkme/a.txt")
    notifyit.EventHandler().process_IN_CLOSE_WRITE(event)
    assert "/tmp/checkme/a.txt" in capsys.readouterr().out


def test_missing_directory_raises(tmp_path):
    with pytest.raises(pyinotify.WatchManagerError):
        notifyit.build_notifier(str(tmp_path / "nope"))


class Recorder(pyinotify.ProcessEvent):
    def my_init(self):
        self.seen = []
    def process_IN_CLOSE_WRITE(self, event):
        self.seen.append(event.pathname)


def test_real_file_triggers_event(tmp_path):    # integration test, needs Linux
    rec = Recorder()
    notifier = notifyit.build_notifier(str(tmp_path), rec)
    target = tmp_path / "new.txt"
    target.write_text("hello")
    assert notifier.check_events(timeout=2000)
    notifier.read_events()
    notifier.process_events()
    notifier.stop()
    assert rec.seen == [str(target)]
