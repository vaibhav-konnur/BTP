from wit import Wit

access_token = "BYYMBOAXSQMN3QNL3A2VGRTKHHPTDTD7"

client = Wit(access_token = access_token)

message_text = "Show me cars from US"





def wit_response(message_text):
	
	response = client.message(message_text)
	# print (response)
	entity = None
	value = None

	try:
		entity = list(response['entities'])[0]
		value = response['entities'][entity][0]['value']
	except:
		pass

	return(entity,value)

print(wit_response(message_text))