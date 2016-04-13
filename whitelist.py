
schema =  {
         'user_id': {
             'type': 'string',
             'required': True,
             'unique': True,
             },
         'ipv4': {
             'type': 'string',
             'required': True,
             },
        'allow': {
            'type': 'bool'
            'default': False
        }
     }

whitelist = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
        'allowed_roles': ['mod', 'admin'],
    },

    'additional_lookup': {
        'url': 'regex("[0-9\.]+")',
        'field': 'ipv4',
        'allowed_roles': ['mod', 'admin'],
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    # Only allow superusers and admins.
    'allowed_roles': ['mod', 'admin'],

    # Finally, let's add the schema definition for this endpoint.
    'schema': schema,
}
