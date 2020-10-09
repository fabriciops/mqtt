config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': 'localhost:1883'    # 0.0.0.0:1883
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False
    }
}