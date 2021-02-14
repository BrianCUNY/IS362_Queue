{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Data Structures - Queue\n"
   ]
  },
  {
   "attachments": {
    "queue.jpeg": {
     "image/jpeg": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0NDQ0NDQ0NDQ0NDQ0NDQ0NDw8NDQ0NFREWFhURFRUYHiggGBolHRUVLTEhJSouLi4uFx8zODMvNygtLisBCgoKDg0OGhAQGy8lHyY2LS0yLjUtLS0rLS03Lys1Li0tLS0tLS0tNS0tLi0uLS0tLS0rKy0rLS0vLS0tKzUtLf/AABEIALIBHAMBEQACEQEDEQH/xAAbAAEBAAIDAQAAAAAAAAAAAAAAAQYHAwQFAv/EAEwQAAEDAQMGCgUJBQUJAAAAAAEAAgMEBRESBgcTITFSFDQ1QVFxdKGyszNhcnORFSIjMlOTscHRF0J1gYMkQ1TC4RYlRWWSlKO00v/EABoBAQACAwEAAAAAAAAAAAAAAAADBgECBQT/xAA2EQEAAQIBCgMHAwQDAAAAAAAAAQIDEQQFITEyNEFxgcEGEmETM1FSkaGxFBXwFiLR8UNj4f/aAAwDAQACEQMRAD8A3VwSPd7ygcEj3e8oHBI93vKDDcssrG2XURwNohPjj0mIzGO7XdddcV0MhzfXlfm8sxGDSqvyvB/ab/ytn/dO/wDhe/8Ap+980fdr7WHqZL5bC0KyOldQNhEjXu0gqHSXYRsuwheTLc115LRFdVUTwbU1xUzzgke73lctucEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKBwSPd7ygcEj3e8oHBI93vKDnQRAQaizu8oQdm/wA6s3h3/k6d0N7gwdWZCyXNvyvTexN4Vws/7vHNJa1t4qoPQICCIKgICAgIIgqCIKgiCoCAgICAgICAgICAgICAgIIgIKg1Fne4/T9mPjVm8O/8nTuhvcGDKzIGSZuOV6b2ZvCuHn/d45pbWtvFU96FQRAQEBBUBAQRAQVAQEBAQEBAQEBAQEBAQEBAQEBAQEBBqPO/x6n7MfGrL4d13OndDe4MFVnQMkzc8r0vsy+FcPP+7xzS2tbeSp70CAgiCoIgqAgIIgqAgIIgqAgICAgICAgICAgICAgICCIKgINR54OPU3ZneNWXw7rudO6G9wYKrOgZHm65XpeqXwriZ+3aOaW1rbzVOegQEBAQRBUBAQEBAQRAQVAQEBAQEBAQEBAQEBAQEBAQEBBqTPBx2l7M/wAasvh3Xc6d0N7gwRWdCyLN3yvSf1fAuJn7do5wkta29FTnoEBB8SSNaL3Oa0dLiAO9BY5GuF7XBw6WkEIPpB8NkaSWhzS5t2IAglt/SOZB9IKgiCoCAg4XVMQNxkjB2XFzQb0HMgICAgICAgICAgICAgICAgICAg1Lnh47Sdmf5gVl8O67nTuhvcGBqzoWRZvOV6T+r4CuJn7do5wkta29FTnoEEQY7l+wGzpLwwkSQYA/U3FpG3a1rOunnDaNU8pePHWvo6uuxaCBxpqVzG0t81O3FLgvcDhulJOq+4XAEm69bRx5x/I7tPhPpP8AJc9NlHO8MgkqIaeQz18IqZNGWl0Lm6Njrvm4nBxvu3TcsROMRPP84M6pmOX3jEjtFzLRmjMog07qMOqGtY6J0mi9Fc7W0u5ieratqeMessTo0+jM1hlUEQVBEFQYXHRaW17SYyGkkYRQmUzE6RrSDiLAGnWRfzjXclGrr2hirX0/y5zbVVjlJmjEXyi6gBEQ+gHzSJC4m6/WRrF15CxTpiPXH7TP+GZ0TPph94hBbNW52hM0THBtoATaNp0uhwYHgE3fvG/m1FJn+2Z9MWYjTEeuH2c2TloTVNWZHz3sksyzqltO0M0YfLpS8tN2L90c63mIjzc+0NcdnkyhasiAgICAgICAgICAgIIgqAg11nMydra2pppKWHStZA9jziDbnF94GtdjNOXW8lmv2mOnBHcpmrUxD/Ya1/8ACf8AkYuz+/ZN8J+iP2UvbyLyStKmtGnnnpxHFHpMTsbTde24agudnPOlnKbPkoxxxb0UTEtsqvpRAQeJlPa9n0jI/lANcyRxEbXxaYFwF+y48yltWK71XlojGWJnB4kWXFgsY6JgDI334o2Upax3W0C4r0/tuVfJLHnp+LnpctLFnfHAzW6WVuBrqchpk1AHWLr9Q1rS5kOUW6fPXTMRBFUTodnKC2LIoZcFZHEJJgJD/ZxIX3HUXG7WetR2cmu3vd044MzVEa3X/aPZH20n3Mn6Kf8Abcq+SWPPT8XbsnLazqydlPBI90rw4tDo3tBuF51lRXsjv2afNcpmIZiqJ1La+WlnUU7qeole2VgaXNbG9wAcLxrHqSzkl69Hmt0zME1RGt0/2j2R9tL9zJ+il/bcq+SWPPT8Xo2FlbQ2hK6Glke6RkZlcHRuZ8zEG33n1kKC9kt2zh7SnDFmKonU6lbl7ZcEskEkzxJE90bwInkBw2i8Bb28hyi5T5qKJmGJqiHSjy7sJj3Ss+bK+/FI2mcJHdbgLypP23Kvkk89Pxerk9a1mVzKgUcbCwEGoboBGHlwJ+cCPnc6817J7lmfLcjBmJx0w8mfLSwCQ14Y7Rh0bQaXEGN2Fo1ahtU9Ob8pqjzRROljzUxofUOXthx3aMlmFuBuCmc3Cy+/CLhqF/Mtv23Kvkljz0sjsO2qevi01M4ujDiy9zSw4ht1FeW5artVeWuMJbROL0VGyICAgICAgICAgICCIKgiCoPPhLuGzgnVwemLG8315bz+Hcg76AgqAg1vnm9HQe+l8srt5h3meU9kd3U1iri87v5Pceo+0xeJc3O26V/zi2t7TK87/Hqfsx8a5Xh3Xc6d0l7gwVWdCyPN1yxSdU3gXEz9u0c4SWtb7zlcsVXsU/lBa+H93q59oLutjK7qJmuaHlSfsEnnRKteIdVvqntcWOZUcpWh2yb8V0sz7pR1/LS5tPNXTaNj5n/qWl1Q+F6qGf8AeKeXeU9rU11N9eT3svjKs2RbvRyhDVrfK9LVt7NFyc/tMv5KjZ43uvp+Hqt7LOFzG4gICAgICAgICAgIIgqAgIOjaLHNdHUMBcYcTZGja+F12IDpIIaR1etB2oZWyND2EOa4XghByICAg1vnm9FQe/k8srt5h3meUo7uprFXF5nesDj1H2mHxLnZ23Sv+cW9G0y3O/x2m7OfGuT4d13OndJe4MEVnQsizecsUf8AW8BXEz9u0c4SWtblzl8sVPsU/lhaeH93q59oLutjC7yJmmaHlWb+Hy+fCq34h2bfVPa4seyq5TtDtcv5LoZn3Snr+WlzaeYuo0bHzPfVtHqh8L1UPEHv6eXeU9rU13P6SX3svjKsuRbvRyhDVrl8L1NW3c0PJ8naZPyVGzxvdXT8PVb2Xep5quW17QpOGyshgpqKeFrY6c4XSmUOaSWXlv0Yu59e1cymP7Zn1w+0N6tExy7uaxsoyeFw1mDhFHUimLogQ2fE0PY5rSdRIOsdKY4xEmGE4O9BlFSysa6Jz5HufLGIWNJmD4/SAt5rtV/WOlP9j5pcpKaZ0LYxMTOJ9HfG4AuiJD2+ogjYnDHqf6GZS0roWTtMhEjZHtZgOlwRm55w7dRSdGnqRp/CR5T0jw50ZkkaKRta1zGOc2SnP7zTz9SToxx4EacMOJV5T0cMQne9wj0TJ3uDSdFC7Y9/QEnROEkaYxey1wIBBBBAII2EdKTGBE4qgICAgICAgICDoyUbmOMlO4Mcdbo3eikPTdzH1hBPlIM1VEb4TvXGSI+sPbs/ncg69sZS0FFTiqqKhjadz2xiVt8jMR2Xlt6Dmsm3KKtbipKqCoF1/wBE9rnAetu0IMJzzehoe0SeU5drMO8zylHd1NYK5PO71hcdo+0w+ILnZ13Sttb2mXZ4OO03Z3eNcjw7rudO6S9wYGrQhZDm95Xo+uXyyuLn7dusJLWtzZzOWKn3dP5YUfh/3FXPtBd1sYXeRszzRcqy/wAOm8+FVvxDs0dU1ri8DKvlO0O1yfgF0MzbpT1/LS5tPLXUaNj5ndlo9UH4PVR8Qe/p5d09rU13Uekl99L4yrJkO72+UIatcvhepq25mh5Pl7TJ+So+eN7q6fh6rey9SKzK+O062uY2mcypgpYGNc+QOYITIcRubrv0mz1LlxMxTMeuP2iG86Zifg682SD9E+QSxyV0lWK2R8rDoJHhuERloN4aG6unnTVhhw7mvHF9iwKmKWlrInUkU8LKmOeJrHMpnQzGNziDffiBibrO3Ws44csDXHX/AMefkpCaqnpKqknp5TTVloB/zsbHMklfrBadR2ELWmMKaeWDE6Zqj1xc7MkqqJlM9j6SWaFtRFIyeN5gkhklxg6jeHNPxWf8RH0ZnvM/V3qnJ+cPDoHQNDqCSikaWOa1t5xBzAOa8nUViqMcfXD7EaMJ+DqDJWojdE5po5Q6mhp6ltRE9zQYxcJI7j0cx1LaZxmfXScIZfGwNa1o2NAA5tQCTOMsRGEPpYZEBAQdWqtGnhcGSzRxucL2te4NJHqCDkpqqKYF0UjZADcSwggHoQcqCoCAgIMQzh5FNtmlEEZhp5DNG985jxPwA6xq2nrKDwLAzJ2TSubJPJU1UrCCDpHUzQekaMhw/wCpBy534mx01nMbeGsmcxt5LjhELgLydZ2bSu1mHeuko7uprJXJ53dsPjtJ2mHxBc/Ou6VtqNpmGeDjlL2d3jXH8O7Vzp3SXuDAlaELIM33K9F7UvluXFz7uvWElrW7Gc3lio91T+BR+H/cVc+0F3Wxdd5EzLNHytJ/Dqjz4FXPEOzR1TWuLwsreVLQ7U/wtXvzNulPX8tbm08pdRo2Nmc/4j1Qfg9VHxB7+nl3T2tTXtT6Wb303mOVkyHdrfKENWuXGvUw2pmsoop7PkErS4NqpCBic0awNtx1qj553urp+Hpt7LM/kal+xb8XfquW3Pkin5mvb7E0zPwcgfJxb6KpqY/U5+nB+9Dj8Cgf2uP7Kob1GGT8we5B9w2gxzgx4dDIdjJBhxeydh/kg7iAgICCIKgIMVytjca2xzG2IycJnA0oJbdoH9GtKNqeU/mCrZ6w56+qqqZlPcKaOaeuihlDGktMT7wHXbb9SRpmI5/iSdETPL8unSZQVBkfSSPZpvlWagZPgDRo207ZwcOzFc67+SRpw6z9JmGJ0TPT7wkVs1gnjjdKxzRajqJ/0YGki0JeD6jfcsROmn1x+2JOjzemH3cVPlJVaoHfSSyWnX0cckbI2kRwtxN+a4gFx/IrMaYp9YmfpOBE6avSYj6xEu1R2naBnpYagsidLDWaRgax5DoyMEl4OokHW1YmdfLFth+cHUpMo62aKkiYMVVNQyVRexsdznNkwABrnDV03a9YWZxw0fCmfrDET8fjMfRlllzSyU8L52NjmdG0ysY4Pa2S75wBG0XrNWGOhiMcNLtLDLXWeb0FD2l/kvXazDvXSUd3U1crk87uWJxyk7TD4gufnXdK+TajahmOeHjlL2d3jXH8O7Vzp3SXuDAlaELIM3/K9F7UvlOXGz7uvWElradnOdyxP7qn8Ch8P+4q59oZu62LLvoWY5oz/vd/8NqfPp1XPEOxRzlNa1y8PK7lS0e1O8LV7szbpT1/LW5tPKXVaNjZnNto9VP+D1UfEHv6eXdPa1Ne1XpZvfzeY5WPId2t8oQ1a5ca9bDbeaDiE3aX/gFR8873V0em3ss7XLbiAgIOOeFkjS17Q5p5j+PqQa7yxzl09gzuonxz1UgibJGCMOEO2AvP1hqOv1FBn9nVOnghmuu0sbJLtt14vuQdlAQEBAQebaVh01VLFNMJjJDfonR1NTBo7xcSBG8AEjn2pGicT0cUmTVG8ND2zuwStna51XVuk0rfquLy/EbuYE3BB8nJazy2ZroC8VE4qZNJLNITUAXCVpc4ljrgBe27UAEjRh6HxdOy8ntVXHVwQ6KSs4TTiKWQuZc0AG+5pa7VzHnSNmPjGLGGmfhLuzZMWdJC+B1JCYpJjUPaAWnTn+8DhrDvWCnw9GY0Y+rnfYdGWQMMDA2nJMIaXNwXi46wdYPODt50nTOJwwdeoyVs2SKGF9HCY6dxdCACwxkm91zgQbjzi+486ccThg9eONrGhrQGtaAGtaLg0DYAEmcR9INdZ5uL0Pan+S9drMW9dJR3dlq5XJ53csbjlJ2mHxBc/Om6V8m1G1DMs8PG6Ts7vGuP4d2rnTukvcGAq0IHv5Acr0PtyeU5cbPu69YS2tp2s53LE/uafwKHw/7irn2hm7rYsu+iZfmk5Zd/DKr/ANimVd8Q+7o5ylta5eNlfyraPaj4GL25l3Snr+WtzaeSuq0bGzN/WtD2af8Azqo+IPf08u6e1qa9q/TT+/n8xyseQbtb5Qhr1y4162rbWZ/iE/an/gFSM873V0eq3ss8XKbiAgICDBM7ORDbZoi6JrRW0wc+nfsxj96InoP43IMiyOe51mUBe0teaWHE1wuc12EXgjpQeygICAgIIgIKgIIgqCIKgiDXueVpNNQ3Nc66rdfhaXXfQv6F18y3KbeU41ThGEo7kYw1bgduSfdv/RWz9Zk/zx9UHll3bFifwul+jk4xD/dv3h6l4c45VZryaummuJnD4tqKZ8zMs8LTwqkIa4jg7x81rna8fqXJzDeot1XPPMRq7pLsTODAMDtyT7t/6Kyfrcn+ePqh8ssgyBjf8r0JwSAB8l5LHgAaJ/OQuTnnKbVzJsKKomcY4pLcTEu1nPY75XmOF5Bhp7iGuI+qegKLMV+3bs1RXVEae0F2JmWK4Hbkn3b/ANF2/wBbk/zx9UfllmOaWN4thzix4aLNqhicxzReZ6a4Xkeo/BcHPt+3cooiiqJ0yltRMS8XLBjvlW0fmP4zeCGOII0bNhuXszRlNqjJaYqqiJ08fVrciZqeRgduSfdv/RdL9bk/zx9WnllsfM2xwdaBLXtBFPdia5t/1+lVfPl2i5epmiYnR3T2owhr2sY7TT/Mk4xP+4/7R3qXeyLKrNOT0RNcY4RxRVUzi4sD/s5Pu3/ovV+tyf54+rXyy21mha4UM2Jrm31LiMTS07B0qnZ2rpryqqqmcY0PRbj+1na5rcQEBAQasyoy7tClr6qmh0Ijhka1mKPE64sa7Wb/AFrvZvzRRlNn2k1TGtFXc8s4PL/aRau9T/df6r2/09a+efs19rLLM3WVNXaM1THUmMiKJj24GYdZcQb9a4+c8gpySqmKZxxSUVeZna5jcQEBAQEEQEFQRAQEFQQtB2gHr1oPnRt3R8AgoY3oHwCAWg7QD1i9BNG3dHwCChoGwD4IBYDtAPWAgmBu6PgEFDQNgA6ggFjegfAIJo27o+AQfQaBsAHUg+cDd0fAILo27o+AQUADYLupBUEQEBBUGhsu+V6/3rPKYrpmPdOsvNd2nhLsI2f5nON1nZ4/GVVfEO3RylPa1S2sq6mEBBUBAQEBAQEBAQEBAQRBUBAQRAQVAQEEQVAQEBAQEBAQaHy85Xr/AHrPKYrnmLdesvNd2ngrso2fZneN1nZ4/Gqt4h27fKeye1xbYVcTCAgICAgIIgIKgICCIKgiCoCCIKgiCoCAgICAgICAgICAgIND5e8r13vI/KYrnmLdes9nnu7TwV2UTPczvHKvszPMVW8Rbdvr2T2uLbKriYQEBAQEEQVAQEEQVBEFQRAQEFQEBAQEBBEFQEBAQEBAQEBBojL/AJXrveR+SxXPMW69Z7PPd2ngLso2eZneO1fZW+YFV/EW1b69k1ni20q2mEBAQRBUEQEBAQEBAQEBAQEBBUBAQRAQEFQEBBEFQEBBEFQaJzgcr13txeSxXPMW69Z7PPd2mPrso2eZnuO1XZW+YFV/EW1b69k1ri20q2mEBAQEBBEFQEEQEBBUBBEBBUEQVBEBBUBBEFQEBBEFQEBAQRBorODyxXe3F5LFcsw7r1ns893aY+u0iZ5me49VdlHmBVfxFtW+vZPZ4ttKtphAQRAQEBAQEBAQEBAQEBBUEQVBEFQRBUEQEFQEBAQEBAQEGt8qcgKutr6iqingayYsIa8PxC6NrTs9ldnIM7fpbXs/Ljpx1o6rfmnF5X7Lq/8AxNL8JF7P6i/6/u19l6smyDyOqLMqJpppopBJCIwIw4EHEDeb+pczOOcP1k0z5cMMezeijys3XNbiAgiAgIKgiAgICAgICAgIKgIIgIKgiAgICAgIKgICAgIIgqAghQVAQRBUH//Z"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![queue.jpeg](attachment:queue.jpeg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is a Queue?\n",
    "\n",
    "#### A Queue is a type of data structure in python that allows us to capture and store data on a first in, first out basis. When creating a queue and adding items to it, this creates a \"stack\" where these items are represented visually as being vertically \"stacked\" ontop of each other or horizontally \"stacked\" as shown above. I will show a brief example of how to create a queue, how to add items to the queue, and how to remove the first item entered into the queue."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# To create a queue, we need to initialize one as follows:\n",
    "queue = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We need to add items to the queue now:\n",
    "queue.append('a1')\n",
    "queue.append('b2')\n",
    "queue.append('c3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a1', 'b2', 'c3']\n"
     ]
    }
   ],
   "source": [
    "# Here we can print to see the created queue:\n",
    "print(queue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a1\n"
     ]
    }
   ],
   "source": [
    "# We are able to remove items from a queue with queue.pop(0) - Starting at 0, pulls first item entered into queue.\n",
    "print(queue.pop(0))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['b2', 'c3']\n"
     ]
    }
   ],
   "source": [
    "# Shows remaining items in the queue after pulling the first item entered in:\n",
    "print(queue)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Queue - Uses\n",
    "\n",
    "#### Some practical uses for implementing a queue would be for things such as scheduling or data collection. In the IT support world, tickets of issues clients have are entered into a queue and are typically pulled and worked on in a first in first out basis. Regarding data collection, if we are pulling data from a website to a file to later manipulate, we can keep better track of the data and save each item as it is captured - this prevents replication and allows us to see at a glance what was already captured in order of capture. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
