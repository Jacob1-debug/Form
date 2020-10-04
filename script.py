# Define your functions
def tea_bot():
  print('Welcome to the cafe!')

  offers=get_offers()
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def print_message():

  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_offers():
  res = input('Get Coupons and Offers: \n[a] Yes \n[b] No Thanks \n>' )

  if res == 'a':
    return 'Your Offer for today is 25% Off use code: NMVOP'
  elif res == 'b':
    return 'Thanks'

  else:
    print_message()
    return get_offers()


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Green Tea \n[b] Kenyan Tea \n[c] White Tea \n> ')
  if res == 'a':
    return 'Green Tea'
  elif res == 'b':
    return 'Kenyan Tea'
  elif res == 'c':
    return 'White Tea'
  else:
    print_message()
    return get_size()




print(tea_bot())

