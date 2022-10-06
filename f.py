import re
s = "Ex|mple Str>ng"
replaced = re.sub('[\/:?*"<>|]', '_', s)
print(replaced)