U
    �^Z
  �                   @   s  d dl Z d dlZd dlT e�d� dZeZdZejedd� e�	e� e
d� e
d	� d
dgZeed��Zeed��Zeed��Zeed��Zze�d�\ZZZW n  ek
r�   dZdZdZY nX e
d� eed��Zeed��Zeed��Zze�d�\ZZZW n" ek
�r&   dZdZdZY nX e
d� eed��Zeed��ZeeeeeeeeeeeeegZg Z e
d� ed�Z!e!dk�s�e!dk�r�ee Z neZ d\Z"Z#e$e"e#d �D ]4Z%e j&e e%d�D ]Z'e
d�(e'�e)dd�d � �qĐq�e
d� e
d!� e
d"� e
d#� e
d$� dS )%�    N)�*�clearaq  
                    /^\/^\
                  _|__|  O|
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~   - ammar1984-
                        ~--______-~                ~-___-~
zh
 Hello, my friends
Must Aldaima find the solution
and we shorten these steps to listen to your time
**
g����MbP?)�tz?***Insert the information about the victim to make a dictionaryz?****If you don't know all the info, just hit enter when asked!
�-�_z> Name:z> Nickname:z
> Surname:z> Birthdate (DD/MM/YYYY):�/� �
z> Girlfriend Name:z> Girlfriend Nickname:z$> Girlfriend Birthdate (DD/MM/YYYY):z> Phone Number:z> Favorite Team:z:Do you want to add some key words about the victim? Y/[N]:�y�Y)�   �   r   )�repeatzpasslist.txt�a)�filez[+] Now making a dictionary...z+[+] Sorting list and removing duplicates...z)[+] Saving dictionary to passwords.txt...z[+] ! Good luck!)*�	itertools�osZV7xStyle�system�pZ	Animationr   ZggZ	SlowIndexZSlowText�printZ	key_words�str�input�nameZnicknameZsurnameZbirthday�split�d�mr
   �
ValueErrorZbest_friendZbest_friend_nicknameZbest_friend_birthdateZd1Zm1Zy1Zphone_numberZfavorite_teamZwordsZpassword_listZxyzZ
min_lengthZ
max_length�range�n�productZxs�join�open� r"   r"   �
Wpy/wpy.py�<module>   sd   




 