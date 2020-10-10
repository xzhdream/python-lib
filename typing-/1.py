from typing import NewType,List

UserId = NewType('UserId', List)
# UserId = List


# Fails at runtime and does not typecheck
class AdminUserId(UserId): pass

AdminUserId([1,2,3])