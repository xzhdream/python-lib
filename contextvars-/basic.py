import contextvars

var = contextvars.ContextVar('var')

token = var.set('new value')
print(token.var,token.old_value,token.MISSING)
# code that uses 'var'; var.get() returns 'new value'.
print(var.get())

ctx: contextvars.Context = contextvars.copy_context()
print(list(ctx.items()))

var.reset(token)

print(var.get())
