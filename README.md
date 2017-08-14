## Hash Blender

This is a small tool to help during black-box application penetration tests where
a hash is found and you want to identify if any parts of the request were used to
create it.

## Use case

You see the following HTTP request:

```http
GET /?id=123&timestamp=1502751161&hash=88c646050d66fb325f4f9cf29f58f328 HTTP/1.1
Host: example
```

And wonder: "Is `hash` the result of performing an MD5 on `id` concatenated with `timestamp`?"

You can test this manually, but... what if they concatenate the two values with a separator?
Which separator? In which order are values concatenated? Are the variable names used?

## Example

Setup the configuration file:

```json
{
 "values": {"id": "123", "timestamp": "1502751161"},
 "hash": {"string": "88c646050d66fb325f4f9cf29f58f328"}
}
```

Run the tool and get the result:

```console
$ ./hash-blender.py config.json
md5("123|1502751161") is "88c646050d66fb325f4f9cf29f58f328"
```