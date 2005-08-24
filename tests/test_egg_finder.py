import os
from paste.script import command

def test_egg_info():
    egg_dir = os.path.join(os.path.dirname(__file__),
                           'fake_packages', 'FakePlugin.egg')
    found = command.find_egg_info_dir(os.path.join(egg_dir, 'fakeplugin'))
    assert found == os.path.join(egg_dir, 'FakePlugin.egg-info')
    found = command.find_egg_info_dir(os.path.dirname(__file__))
    assert found == os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'PasteScript.egg-info')
    
def test_resolve_plugins():
    plugins = ['FakePlugin']
    all = command.resolve_plugins(plugins)
    assert all
    assert len(all) == 2

def test_find_commands():
    all = command.resolve_plugins(['PasteScript', 'FakePlugin'])
    commands = command.get_commands(all)
    print commands
    assert 'help' in commands
    assert 'testcom' in commands
    
