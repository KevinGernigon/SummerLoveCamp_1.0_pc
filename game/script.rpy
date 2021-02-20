#Déclarez sous cette ligne les images, avec l'instruction 'image'
image image_alix_normal = "../images/alix_normal.png"
image image_alix_clin = "../images/alix_clin.png"
image image_alix_sourire = "../images/alix_sourire.png"
image image_alix_enerve = "../images/alix_enerve.png"
image image_alix_pleure = "../images/alix_pleure.png"
image image_alix_gene = "../images/alix_gene.png"
image image_rebecca_normal = "../images/rebecca_normal.png"
image image_rebecca_enerve = "../images/rebecca_enerve.png"
image image_rebecca_gene = "../images/rebecca_gene.png"
image image_rebecca_sourire = "../images/rebecca_sourire.png"
image image_rebecca_triste = "../images/rebecca_triste.png"
image image_rebecca_blush = "../images/rebecca_blush.png"
image image_ema_normal = "../images/ema_normal.png"
image image_ema_triste = "../images/ema_triste.png"
image image_ema_sourire = "../images/ema_sourire.png"
image image_ema_enerve = "../images/ema_enerve.png"
image image_ema_gene = "../images/ema_gene.png"
image image_theo_normal = "../images/theo_normal.png"
image image_theo_muscle = "../images/theo_muscle.png"
image image_theo_muscle_inverse = "../images/theo_muscle_inverse.png"
image image_theo_blush = "../images/theo_blush.png"
image image_theo_sourire = "../images/theo_sourire.png"
image image_theo = "../images/male_character_placeholder.png"
image fond_cuisine_jour = "../images/cuisine.png"
image fond_cantine_jour = "../images/cantine_jour.jpg"
image soupe_tomate = Image("../images/soupe.png", xalign = 0.5, yalign = 0.5)
image oeuf_mayo = Image("../images/oeuf_mayo.png", xalign = 0.5, yalign = 0.5)
image pates_bolo = Image("../images/plat_bolo.png", xalign = 0.5, yalign = 0.5)
image pates_carbo = Image("../images/plat_carbo.png", xalign = 0.5, yalign = 0.5)
image burger = Image("../images/burger.png", xalign = 0.5, yalign = 0.5)
image mousse = Image("../images/mousse.png", xalign = 0.5, yalign = 0.5)
image salade = Image("../images/salade.png", xalign = 0.5, yalign = 0.5)
image fond_rythm = "../images/fond_rythm.png"
image nenuphar_1 = Image("../images/nenuphar.png", xpos = 1000, ypos = 250)
image nenuphar_2 = Image("../images/nenuphar_2.png", xpos = 1000, ypos = 410)
image nenuphar_3 = Image("../images/nenuphar_3.png", xpos = 1000, ypos = 560)

image fond_chambre_jour = "../images/dortoir_jour.jpg"
image fond_chambre_matin = "../images/dortoir_matin.jpg"
image fond_chambre_nuit = "../images/dortoir_nuit.jpg"
image fond_noir = "../images/fond_noir.png"
image fond_colo_jour = "../images/colo_jour.jpg"
image fond_colo_matin = "../images/colo_matin.jpg"
image fond_colo_nuit = "../images/colo_nuit.jpg"
image fond_couloir_jour = "../images/couloir_jour.jpg"
image fond_couloir_nuit = "../images/couloir_nuit.jpg"
image fond_foret_jour = "../images/foret_jour.jpg"
image fond_foret_matin = "../images/foret_matin.jpg"
image fond_foret_nuit = "../images/foret_nuit.jpg"
image fond_boom_jour = "../images/lacboom_jour.jpg"
image fond_boom_nuit = "../images/lacboom_nuit.jpg"
image fond_boom_fete = "../images/lacboom_nuitft.jpg"
image fond_journal = "../images/fond_journal.jpg"
image bad_end = "../images/bad_end.jpg"

#endings
image fin_rebecca = "../images/end_rebecca.jpg"
image fin_ema = "../images/end_ema.jpg"
image fin_alix = "../images/end_alix.jpg"
image fin_theo = "../images/end_theo.jpg"
image credits = "../images/credits.png"

# Déclarez les personnages utilisés dans le jeu.
define perso_joueur = Character("Moi", color="#FFFFFF")
define perso_theo = Character("Théo Stéronne", color="#c8ffc8")
define perso_alix = Character("Alix", color="#FFAE00")
define perso_rebecca = Character("Rebecca", color="#8300FF")
define perso_ema = Character("Ema", color="#FBFF00")
define perso_meta = Character("Les filles", color="#F90E00")

default halters = 0
#screens

screen show_oeuf:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oeuf.png"
        action Jump("Oeuf_Oeuf")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/viande.png"
        action Jump("Oeuf_Viande")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/kiwi.png"
        action Jump("Oeuf_Kiwi")

screen show_mayo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/creme_fraiche.png"
        action Jump("Mayo_Creme_Fraiche")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/mayo.png"
        action Jump("Mayo_Mayo")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/fromage.png"
        action Jump("Mayo_Fromage")

#recette soupe tomate
screen show_tomate:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oeuf.png"
        action Jump("Tomate_Oeuf")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/tomate.png"
        action Jump("Tomate_Tomate")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/lardons.png"
        action Jump("Tomate_Lardons")

screen show_oignon:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oignon.png"
        action Jump("Oignon_Oignon")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/kiwi.png"
        action Jump("Oignon_Kiwi")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/chocolat.png"
        action Jump("Oignon_Chocolat")

#recette pates bolo
screen show_viande_bolo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/viande.png"
        action Jump("Viande_Bolo_Viande")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/sucre.png"
        action Jump("Viande_Bolo_Sucre")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pomme.png"
        action Jump("Viande_Bolo_Pomme")

screen show_pates_bolo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/pates.png"
        action Jump("Pates_Bolo_Pates")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Pates_Bolo_Pain")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pasteque.png"
        action Jump("Pates_Bolo_Pasteque")

screen show_oignon_bolo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oignon.png"
        action Jump("Oignon_Bolo_Oignon")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Oignon_Bolo_Pain")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/chocolat.png"
        action Jump("Oignon_Bolo_Chocolat")

screen show_tomate_bolo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/tomate.png"
        action Jump("Tomate_Bolo_Tomate")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/sucre.png"
        action Jump("Tomate_Bolo_Sucre")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/oeuf.png"
        action Jump("Tomate_Bolo_Oeuf")

#recette pates carbo
screen show_lardons:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/lardons.png"
        action Jump("Lardons_Lardons")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/chocolat.png"
        action Jump("Lardons_Chocolat")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pomme.png"
        action Jump("Lardons_Pomme")

screen show_pates_carbo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/pates.png"
        action Jump("Pates_Carbo_Pates")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Pates_Carbo_Pain")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/kiwi.png"
        action Jump("Pates_Carbo_Kiwi")

screen show_oignon_carbo:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oignon.png"
        action Jump("Oignon_Carbo_Oignon")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/sucre.png"
        action Jump("Oignon_Carbo_Sucre")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pasteque.png"
        action Jump("Oignon_Carbo_Pasteque")

screen show_creme_fraiche:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/creme_fraiche.png"
        action Jump("Creme_Fraiche_Creme_Fraiche")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Creme_Fraiche_Pain")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/chocolat.png"
        action Jump("Creme_Fraiche_Chocolat")

#recette burger

screen show_pain:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Pain_Pain")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pates.png"
        action Jump("Pain_Pates")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/lardons.png"
        action Jump("Pain_Lardons")

screen show_viande_burger:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/viande.png"
        action Jump("Viande_Burger_Viande")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/oeuf.png"
        action Jump("Viande_Burger_Oeuf")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/kiwi.png"
        action Jump("Viande_Burger_Kiwi")

screen show_tomate_burger:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/tomate.png"
        action Jump("Tomate_Burger_Tomate")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pomme.png"
        action Jump("Tomate_Burger_Pomme")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/creme_fraiche.png"
        action Jump("Tomate_Burger_Creme_Fraiche")

screen show_fromage:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/fromage.png"
        action Jump("Fromage_Fromage")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pates.png"
        action Jump("Fromage_Pates")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pasteque.png"
        action Jump("Fromage_Pasteque")

#recette mousse au chocolat

screen show_chocolat:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/chocolat.png"
        action Jump("Chocolat_Chocolat")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/fromage.png"
        action Jump("Chocolat_Fromage")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/oignon.png"
        action Jump("Chocolat_Oignon")

screen show_mousse_oeuf:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/oeuf.png"
        action Jump("Oeuf_Mousse_Oeuf")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/pates.png"
        action Jump("Oeuf_Mousse_Pates")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/tomate.png"
        action Jump("Oeuf_Mousse_Tomate")

screen show_sucre:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/sucre.png"
        action Jump("Sucre_Sucre")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/fromage.png"
        action Jump("Sucre_Fromage")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Sucre_Pain")

#recette salade de fruits (joli joli)

screen show_pomme:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/pomme.png"
        action Jump("Pomme_Pomme")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/fromage.png"
        action Jump("Pomme_Fromage")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pain.png"
        action Jump("Pomme_Pain")

screen show_kiwi:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/kiwi.png"
        action Jump("Kiwi_Kiwi")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/viande.png"
        action Jump("Kiwi_Viande")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/creme_fraiche.png"
        action Jump("Kiwi_Creme_Fraiche")

screen show_pasteque:
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle "../images/mayo.png"
        action Jump("Pasteque_Mayo")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "../images/oignon.png"
        action Jump("Pasteque_Oignon")
    imagebutton:
        xalign 0.75
        yalign 0.5
        idle "../images/pasteque.png"
        action Jump("Pasteque_Pasteque")

#halteres
default nombre_recup = 0

screen halter_1:
    imagebutton:
        xalign 0.8
        yalign 0.6
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_1"), Hide("nombre_halters"), Show("nombre_halters")]

transform zoom_halter_2:
    zoom 3.0

screen halter_2:
    imagebutton:
        xalign 0.01
        yalign 0.6
        at zoom_halter_2
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_2"), Hide("nombre_halters"), Show("nombre_halters")]

transform rotate_halter_3:
    rotate 160
    zoom 0.7

screen halter_3:
    imagebutton:
        xalign 0.03
        yalign 0.6
        at rotate_halter_3
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_3"), Hide("nombre_halters"), Show("nombre_halters")]

screen halter_4:
    imagebutton:
        xalign 0.8
        yalign 0.7
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_4"), Hide("nombre_halters"), Show("nombre_halters")]

screen halter_5:
    imagebutton:
        xalign 0.68
        yalign 0.65
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_5"), Hide("nombre_halters"), Show("nombre_halters")]

screen halter_6:
    imagebutton:
        xalign 0.95
        yalign 0.8
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_6"), Hide("nombre_halters"), Show("nombre_halters")]


transform zoom_halter_7:
    zoom 0.5

screen halter_7:
    imagebutton:
        xalign 0.7
        yalign 0.4
        at zoom_halter_7
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_7"), Hide("nombre_halters"), Show("nombre_halters")]

transform rotate_halter_8:
    rotate 165

screen halter_8:
    imagebutton:
        xalign 0.05
        yalign 0.30
        at rotate_halter_8
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_8"), Hide("nombre_halters"), Show("nombre_halters")]

screen halter_9:
    imagebutton:
        xalign 0.74
        yalign 0.7
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_9"), Hide("nombre_halters"), Show("nombre_halters")]

transform rotate_halter_10:
    rotate 150

screen halter_10:
    imagebutton:
        xalign 0.16
        yalign 0.73
        at rotate_halter_10
        idle "../images/halters.png"
        hover "../images/halters_hover.png"
        action [SetVariable("nombre_recup", nombre_recup + 1), Hide("halter_10"), Hide("nombre_halters"), Show("nombre_halters")]



screen nombre_halters:
    text "%d" % nombre_recup:
        xalign 0.9
        yalign 0.03
    image "../images/halters.png":
        xalign 0.98
        yalign 0.02

#pong

init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery
            self.computerx = self.playery
            self.computerz = (self.COURT_BOTTOM - self.COURT_TOP) / 4

            # The speed of the computer.
            self.computerspeed = 380.0
            self.computerspeed_2 = 300
            self.computerspeed_3 = 100

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            cspeed_2 = self.computerspeed_2 * (dtime/3)
            if abs(self.by - self.computerx) <= cspeed_2:
                self.computerx = self.by
            else:
                self.computerx += cspeed_2 * (self.by - self.computerx) / abs(self.by - self.computerx)

            cspeed_3 = self.computerspeed_3 * (dtime/3)
            if abs(self.by - self.computerz - 2) <= cspeed_3:
                self.computerz = self.by
            else:
                self.computerz += cspeed_3 * (self.by - self.computerz -2) / abs(self.by - self.computerz -2)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy


            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy


            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - (self.PADDLE_X * 1.5) - self.PADDLE_WIDTH, self.computerx, width - (self.PADDLE_X * 1.5) - self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)
            paddle((self.PADDLE_X * 1.5), self.computerz, (self.PADDLE_X *1.5) + self.PADDLE_WIDTH)
            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

init python:
    config.screen_width=1280
    config.screen_height=720
    import time
    import pygame

    class Rhythm(object):
        def __init__(self, sprite, speed, delay, valeurX, valeurY):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = valeurX
            self.show.y = valeurY
            self.moving = False

        def update(self):
            if store.t + self.delay < time.time():
                self.moving = True
                self.x = self.x + self.speed
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    def sprites_update(st):
        for sprite in sprites[:]:
            sprite.update()
            if sprite.x > config.screen_width:
                store.misses += 1
                sprite.show.destroy()
                sprites.remove(sprite)
                renpy.restart_interaction()
        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                hit = False
                for sprite in sprites[:]:
                    if sprite.moving:
                        if int(sprite.x) < 1100:
                            if int(sprite.x) > 800:
                                store.hits += 1
                                hit = True
                                sprite.show.destroy()
                                sprites.remove(sprite)
                                renpy.restart_interaction()
                                break
                if not hit:
                    store.misses += 1
                renpy.restart_interaction()


screen show_game:
    text "Ratés: [misses], Réussis: [hits]!" xalign 0.5 yalign 0.9

screen pong():

    default pong = PongDisplayable()

    add pong

    text _("Vous"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 20

    text _("Alix"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 20

    text _("Rebecca"):
        xpos 360
        xanchor 0.5
        ypos 25
        size 20

    text _("Ema"):
        xpos (1280 - 360)
        xanchor 0.5
        ypos 25
        size 20


    if pong.stuck:
        text _("Click to Begin"):
            xalign 0.5
            ypos 50
            size 40

init python:

    class PongDisplayable_2(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery
            self.computerz = (self.COURT_BOTTOM - self.COURT_TOP) / 4

            # The speed of the computer.
            self.computerspeed = 500.0
            self.computerspeed_2 = 300


            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime * 50
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            cspeed_2 = self.computerspeed_2 * (dtime/3)
            if abs(self.by - self.computerz - 2) <= cspeed_2:
                self.computerz = self.by
            else:
                self.computerz += cspeed_2 * (self.by - self.computerz -2) / abs(self.by - self.computerz -2)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy


            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy


            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        self.bspeed *= 20

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)
            paddle((self.PADDLE_X * 1.5), self.computerz, (self.PADDLE_X *1.5) + self.PADDLE_WIDTH)
            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong_2():

    default pong = PongDisplayable_2()

    add pong

    text _("Vous"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 20

    text _("Théo Steronne"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    text _("Rebecca"):
        xpos 360
        xanchor 0.5
        ypos 25
        size 20


    if pong.stuck:
        text _("Cliquez pour commencer"):
            xalign 0.5
            ypos 50
            size 25

screen timeup_alix():
    timer 30.0 action Jump("suite_rythm_alix")
screen timeup_rebecca():
    timer 30.0 action Jump("suite_rythm_rebecca")
screen timeup_ema():
    timer 30.0 action Jump("suite_rythm_ema")

#variables affinités
default affinite_rebecca = 50
default affinite_ema = 50
default affinite_alix = 50

# Le jeu commence ici
label start:

# Monologue début
    scene fond_noir
    perso_joueur "(J’avais hâte que ces grandes vacances arrivent. Les journées passées au lycée se faisaient de plus en plus longues. J’ai bien cru que j'allais mourir d’ennui avant l’été.)"
    perso_joueur "(J’avais de grands projets pour cette période de l’année. Avec ce tout nouveau rpg en ligne qui venait de sortir, j'étais assuré de passer tout mon été à m’éclater sans personne pour venir perturber mon havre de paix.)"
    show image_ema_sourire
    perso_joueur "(Mais c’était sans compter sur Ema. Une fille que je côtoie déjà depuis la maternelle.)"
    perso_joueur "(Elle a toujours eu cette tendance surprotectrice à mon égard, elle excelle donc dans l’art de perturber ma petite vie tranquille.)"
    hide image_ema_sourire
    perso_joueur "(Ce coup-ci elle a décidé de m’embarquer dans une colo de vacances soit-disant parce qu'elle avait pitié de moi et de ma situation sociale discutable.)"
    perso_joueur "(Et je n’avais aucun allié pour me sortir de ce pétrin. Aucun ami avec qui je pouvais prétexter vouloir passer du temps.)"
    perso_joueur "(Quand à mes parents, ils ont tout de suite sauté sur cette occasion de me faire sortir de chez moi.)"

# Arrivée colo/Renconte Alix

    scene fond_colo_jour
    show screen nombre_halters
    show screen halter_1
    show image_theo_sourire
    play music "../audio/musique_accueil.mp3"

    perso_theo "Hey, salut gamin ! Bienvenue à la colo des Rainettes ! Tu fais partie de cette grande famille maintenant !"
    perso_theo "Moi c’est Théo !"
    hide image_theo_sourire
    show image_theo_muscle
    perso_theo "Moi c’est Théo ! Steronne !"
    hide image_theo_muscle
    show image_theo_muscle_inverse
    perso_theo "Moi c’est Théo ! Steronne ! BANG ! BANG !"
    hide image_theo_muscle_inverse
    show image_theo_normal
    perso_theo "Hum Hum..."
    perso_theo "Tout d’abord vas mettre tes affaires dans le dortoir ensuite tu pourras te diriger vers la cantine pour remplir ton petit ventre de grenouille !"
    perso_theo "Et si tu as un soucis hésite pas à ..."
    perso_joueur "(Tout d’un coup, j’entends quelqu’un arriver très vite derrière moi…)"
    perso_joueur "(AÏE! Hey qui m’a tapé dans le dos?)"
    hide image_theo_normal
    show image_alix_sourire
    perso_alix "Salut !"
    $ perso_alix("T’es nouveau ? Comment tu vas ? Tu t’appelles comment ?", interact = False)
    $ result_1 = renpy.display_menu([ ("Je vais bien, je m'appelle Anthony et toi ?", "un"), ("Salut… moi c’est Anthony","deux"), ("Moi c’est Anthony mais calme toi un peu.","trois")])
    if result_1 == "un" or result_1 == "deux":
        hide image_alix_sourire
        show image_alix_clin
        perso_alix "Ah super ! Moi c’est Alix ! C’est vraiment cool que tu ailles bien. On se reverra sûrement pendant la colo."
        $ perso_alix("J'espère qu’on va bien s’entendre tous les deux, en tous cas t’as l’air sympa ! Tu vas faire quoi là, tu veux de l’aide ?", interact = False)
        $ result_2 = renpy.display_menu([ ("Oh non t’inquiète pas ça va le faire, j’ai juste à déposer mes affaires dans le dortoir.", "un"), ("Oh non, j’ai juste des affaires à déposer.","deux")])
        if result_2 == "un":
            $ affinite_alix += 10
            hide image_alix_clin
            show image_alix_normal
            perso_alix "Oh bon... je te laisse alors. Je vais pas te déranger plus longtemps."
            hide image_alix_normal
            show image_alix_sourire
            perso_alix "En plus ton sac a l’air lourd. Va vite le déposer. Allez, salut ! On se voit à la cantine plus tard."
        if result_2 == "deux":
            hide image_alix_clin
            show image_alix_pleure
            perso_alix "Oh bon... je te laisse alors. Je vais pas te déranger plus longtemps."
            hide image_alix_pleure
            show image_alix_normal
            perso_alix " En plus ton sac a l’air lourd. Va vite le déposer. Allez, salut ! On se voit à la cantine plus tard."
    if result_1 == "trois":
        $ affinite_alix -= 10
        hide image_alix_sourire
        show image_alix_pleure
        perso_alix "Ah ok… Moi c’est Alix… heu… je te laisse du coup… j'espère que… non rien en fait…"
    hide image_alix_normal
    hide image_alix_sourire
    hide image_alix_pleure
    hide screen halter_1

# Rencontre Ema

    scene fond_couloir_jour
    show image_ema_normal
    show screen halter_7
    stop music
    play music "../audio/theme_global.mp3"
    perso_ema "Yo Bambi, T'es enfin arrivé ! Ca fait longtemps qu’on s’est pas vu, ça fait plais' de te revoir !"
    $ perso_joueur ("Ah ouais ça fait un bail Panpan.", interact = False)
    $ result_3 = renpy.display_menu([ ("Moi aussi ça me fait plaisir de te revoir, qu’est-ce que tu deviens ?", "un"), ("Je vais juste ranger mes affaires, on se revoit à la cantine.","deux"), ("J’ai pas le temps de te parler, j'ai autre chose à faire.","trois")])
    if result_3 == "un":
        $ affinite_ema += 10
        perso_ema "Moi j’ai été virée de mon lycée, sous prétexte d'avoir encore “amoché” un des débris de ma classe."
        $ perso_ema ("Mais bon moi je m’en fous tant que je peux créer mes sons tranquille… Tu t'es déjà fait virer de ton lycée ?", interact = False)
        $ result_4 = renpy.display_menu([ ("Ouais ça m'est déjà arrivé plusieurs fois déjà.", "un"), ("Ouais ça m’est arrivé une fois.","deux"), ("Non, jamais.","trois")])
        if result_4 == "un":
            $ affinite_ema += 10
            perso_ema "Oh le malade que t’es Bambi !"
        if result_4 == "deux":
            perso_ema "Oh t’es pas si blanc que ça Bambi !"
        if result_4 == "trois":
            perso_ema "Ah ouais Bambi c’est pas qu’un surnom en fait."
        perso_ema "Ah j’ai trop la dalle, c’est l’heure de manger en plus ! Je vais à la cantine, tu viens ?"
        perso_joueur "Je dépose mon sac, j’arrive."
    if result_3 == "deux":
        perso_ema "Ok on fait comme ça, je t’attends pas j’ai trop la dalle !"
    if result_3 == "trois":
        $ affinite_ema -= 10
        perso_ema "Ah.. Ok… ­À plus tard…"
    hide image_ema_normal
    hide screen halter_7

# Rencontre Rebecca

    scene fond_chambre_jour
    show fond_chambre_jour
    show screen halter_8
    perso_joueur "(J’ai enfin trouvé ma chambre... Il y a de quoi se perdre dans ce dortoir!)"
    perso_joueur "(Le dortoir auquel je suis assigné est très grand. Il y avait cinq lits disposés dans la pièce. On m’a dit que j'étais sur le deuxième lit à gauche.)"
    perso_joueur "(Tiens... Quelqu’un est déjà là, assis sur mon lit...  Elle ne semble pas m’avoir remarqué.)"
    perso_joueur "(Je m’approche doucement, je commence à discerner un visage derrière ses cheveux noirs. Elle semble avoir un pot de peinture noire sur son visage...)"
    perso_joueur "Euh, salut... je crois que t’es assise sur mon lit... Je suis nouveau, je vais en avoir besoin."
    show image_rebecca_gene
    perso_rebecca "Ah... p-pardon, je suis vraiment désolée..."
    hide image_rebecca_gene
    show image_rebecca_blush
    perso_joueur "(Je la voyais enfin de face. Son visage est devenu rouge comme une tomate, le fait que je lui adresse la parole semble lui faire perdre ses moyens...)"
    perso_joueur "(Elle semblait avoir prit mon lit pour s’asseoir et lire tranquillement.)"
    $ perso_joueur ("(Mmmh ? C’est quoi cette poupée qu’elle tient dans la main droite. Elle la serre très fort contre elle.)", interact = False)
    $ result_5 = renpy.display_menu([ ("Je suis désolé de t’avoir fait peur, c'était pas ce que je voulais faire... Moi, c’est Anthony, et toi?", "un"), ("Merci de m’avoir rendu mon lit. Je m’appelle Anthony","deux"), ("...","trois")])
    if result_5 == "un":
        $ affinite_rebecca += 10
        hide image_rebecca_blush
        show image_rebecca_sourire
        perso_rebecca "Y’a- Y’a pas de souci... c’est moi qui n’aurait pas dû m’asseoir ici. Je-Je m’appelle Rebecca. Enchantée de faire ta connaissance..."
    if result_5 == "deux":
        perso_rebecca "De-de rien... euh... Moi c’est Rebecca."
    if result_5 == "trois":
        $ affinite_rebecca -= 10
        hide image_rebecca_blush
        show image_rebecca_gene
        perso_rebecca "Vraiment désolée euh... Je m’appelle Rebecca, comment tu t’appelles ?"
        perso_joueur "Je m’appelle Anthony."
    hide image_rebecca_gene
    hide image_rebecca_sourire
    hide image_rebecca_blush
    show image_rebecca_normal
    perso_joueur "(Cette fille m’a l’air très timide... J’ai l’impression que c’est une gothique avec cette tenue.)"
    perso_joueur "(Coupe de cheveux à mèches violettes, la peau blanche comme neige, vêtements noirs... Tout y est.)"
    perso_joueur "(Je commence alors à déballer mes affaires, je vais ranger mes affaires dans mon armoire et commencer à préparer mon lit.)"
    if result_5 == "un" or result_5 == "deux":
        hide image_rebecca_normal
        show image_rebecca_blush
        $ perso_rebecca ("Du coup, on sera voisin de chambre... J'espère qu’on s’entendra bien...", interact = False)
        $ result_6 = renpy.display_menu([ ("J'espère aussi, tu as l’air sympa. Tu me feras faire un tour de toute la colo un de ces jours.", "un"), ("L’avenir nous le dira, j'espère que tu es sympa.","deux"), ("Ouais pourquoi pas... Je dois ranger mes affaires vite fait","trois")])
        if result_6 == "un":
            $ affinite_rebecca += 10
            perso_rebecca "..."
        if result_6 == "trois":
            $ affinite_rebecca -= 10
            hide image_rebecca_blush
            show image_rebecca_enerve
            perso_rebecca "D’a-D’accord..."
    if result_5 == "trois":
        $ perso_rebecca ("Euh... Tu veux que je t’aide à t’installer ?", interact = False)
        $ result_7 = renpy.display_menu([ ("Ouais si tu veux, j’ai tellement de trucs à déballer que de l’aide ne serait pas de refus", "un"), ("Non ça devrait aller ne t'inquiète pas...","deux"), ("Non, je vais me débrouiller. Je peux m’en occuper tout seul...","trois")])
        if result_7 == "un":
            $ affinite_rebecca += 10
            hide image_rebecca_normal
            show image_rebecca_sourire
            perso_joueur "(Je donne quelques affaires à Rebecca pour qu’elle m’aide à préparer mon petit nid douillet. Elle a l’air très sympa malgré son apparence.)"
        if result_7 == "trois":
            $ affinite_rebecca -= 10
            hide image_rebecca_normal
            show image_rebecca_gene
            perso_rebecca "..."
    perso_joueur "(Tout d’un coup, j’entends une voix forte et grave crier dans le couloir, c'était Théo qui semblait nous appeler.)"
    perso_theo "EH MES GRENOUILLES, ON VA BIENTÔT MANGER, DESCENDEZ NOUS AIDER À METTRE LA TABLE ET PRÉPARER À MANGER"
    perso_joueur "(Je crois qu'il est temps de descendre à la cantine pour s’occuper des tâches journalières.)"
    perso_joueur "(Je finis de ranger mes affaires et je commence à me diriger vers la cantine. Rebecca me suis au loin.)"
    hide image_rebecca_gene
    hide image_rebecca_sourire
    hide image_rebecca_enerve
    hide image_rebecca_blush
    hide screen halter_8

#mini jeu la BOUFFE

    scene fond_cuisine_jour
    show screen halter_2
    perso_joueur "(Il va bientôt être l'heure de manger. J'avoue que ces quelques heures de bus m'ont bien donné la dalle.)"
    perso_joueur "(Je me demande bien qu'est-ce qu'il y a pour ce midi.)"
    show image_theo_normal
    perso_theo "On se bouge les grenouilles ! Ici on prépare à manger nous même ! Donc retroussez vos manches et mettez vous aux fourneaux !"
    perso_theo "Comme d'habitude, choisissez un partenaire pour être plus…"
    hide image_theo_normal
    show image_theo_muscle
    perso_theo "Comme d'habitude, choisissez un partenaire pour être plus… Efficace !"
    hide image_theo_muscle
    perso_joueur "(Si j'ai bien compris, il va falloir que je me salisse les mains. Mais le vrai problème c'est que je ne sais pas du tout avec qui je vais me mettre.)"
    perso_joueur "(Je vais surement finir avec Ema. c'est la seule personne que je connais ici.)"
    perso_joueur "(Rebecca, toujours en train de me suivre, viens d'arriver dans la pièce.)"
    perso_joueur "(A voir son air gênée, elle est peut-être dans la même situation que moi.)"
    perso_joueur "(Alors que je m'apprêtais à l'approcher, quelqu'un me sauta dessus pour m'adresser la parole)"
    show image_alix_normal
    perso_alix "Hey ! T'es tout seul le nouveau ? Si tu as besoin d'un partenaire je peux t'aider si tu veux."
    hide image_alix_normal
    show image_alix_sourire
    $ perso_alix ("Même si je suis pas très bonne en cuisine, l'important c'est de s'amuser.", interact = False)
    $ result_8 = renpy.display_menu([ ("Choisir Alix", "un"), ("Choisir Ema","deux"), ("Choisir Rebecca","trois"), ("Rester seul","quatre")])
    if result_8 == "un":
        $ affinite_alix += 10
        perso_joueur "Ok, je veux bien faire la cuisine avec toi."
        perso_joueur "Mais je te préviens moi aussi je suis pas très bon en cuisine."
        hide image_alix_sourire
        show image_alix_clin
        perso_alix "Super on va bien s'amuser tu va voir"
        perso_joueur "(Et c'est ainsi qu'on commença à cuisiner.)"
        perso_joueur "(Comme prévu, elle ne savait comment tenir une cuisine.)"
        perso_joueur "(Heureusement on avait toute les recettes à notre disposition.)"
        hide image_alix_clin
    if result_8 == "deux":
        $ affinite_ema += 10
        perso_joueur "Non désolé, je suis déjà avec quelqu'un."
        hide image_alix_sourire
        show image_alix_clin
        perso_alix "Ok, pas de problème on se revoit pour manger alors."
        hide image_alix_clin
        perso_joueur "(Après qu'Alix soit ressorti de la pièce, j'attendis dans un coin de la pièce qu'Ema pointe le bout de son nez.)"
        show image_ema_normal
        perso_ema "Ah tu es là ! Tu as trouvé un partenaire ?"
        perso_joueur "Non… je t'attendais."
        hide image_ema_normal
        show image_ema_sourire
        perso_ema "Ahah sérieux ? Dis plutôt que tu avais peur d'adresser la parole à qui que ce soit!"
        perso_ema "Allez viens, il va pas se préparer tout seul ce repas !"
        hide image_ema_sourire
    if result_8 == "trois":
        $ affinite_rebecca += 10
        perso_joueur "Non désolé, je suis déjà avec quelqu'un."
        hide image_alix_sourire
        show image_alix_clin
        perso_alix "Ok, pas de problème on se revoit pour manger alors."
        hide image_alix_clin
        perso_joueur "(J'attendis qu'Alix soit ressorti de la pièce pour me diriger vers Rebecca.)"
        show image_rebecca_normal
        perso_joueur "Euh Rebecca, tu es toute seule ?"
        #si affinité > 50
        if affinite_rebecca >= 50 :
            hide image_rebecca_normal
            show image_rebecca_gene
            perso_rebecca "Euh oui… Je cherchais quelqu'un justement."
            perso_rebecca "Et toi ? Tu n'es avec personne ?"
            perso_joueur "Non justement je pensais qu'on pourrais se mettre ensemble"
            hide image_rebecca_gene
            show image_rebecca_sourire
            perso_rebecca "Ok je te suis alors"
            perso_joueur "(Et c'est ainsi qu'on commença à cuisiner.)"
            perso_joueur "(Elle semblait un peu mal à l'aise mais comme elle n'as pas hésité à accepter de m'accompagner. C'est qu'elle doit juste être un peu timide.)"
        if affinite_rebecca < 50:
            perso_rebecca "Oui... pourquoi ?"
            perso_joueur "C'était pour savoir si on pouvait cuisiner ensemble"
            perso_rebecca "Ah bon, tu es sûr ?"
            perso_joueur "Oui, enfin pourquoi pas ? Je suis tout seul moi aussi de toute façon."
            perso_rebecca "Bon d'accord, je te suis"
            perso_joueur "(Et c'est ainsi qu'on commença à cuisiner.)"
            perso_joueur "(Elle semblait un peu mal à l'aise sans doute à cause de la façon dont je lui ai parlé tout à l'heure.)"
            hide image_rebecca_sourire
            hide image_rebecca_normal
    if result_8 == "quatre":
        $ affinite_ema -= 20
        $ affinite_rebecca -= 20
        $ affinite_alix -= 20
        perso_joueur "Non désolé, je préfère largement rester seul !"
        hide image_alix_sourire
        show image_alix_enerve
        perso_alix "Pff... T'es pas très drôle toi."
        hide image_alix_enerve
        perso_joueur "(Je m'en fiche de faire mauvaise impression, je n'avais clairement pas la tête à me taper des corvées et en plus devoir sociabiliser.)"
        perso_joueur "(Je parti donc m'assoir dans un coin de la pièce pour attendre que les choses se passent.)"
        show image_theo_normal
        perso_theo "Bah voyons mon ptit têtard que fais tu assis ici ?"
        perso_theo "Je vois que tu n'as pas trouvé de compagnon. Ne t'en fait pas, c'est normal le premier jour."
        perso_theo "Ca ira bien mieux la prochaine fois !"
        hide image_theo_normal
        show image_theo_sourire
        perso_theo "Allez viens ! Je serais ton partenaire pour cette fois."
        perso_joueur "(Et c'est ainsi qu'on commença à cuisiner.)"
        perso_joueur "(En plus d'avoir un corps parfaitement sculpté, il était très doué en cuisine.)"
        perso_joueur "(Il me montra toute les recettes et m'incita à me débrouiller seul pour la préparation des plats)"
        hide image_theo_sourire
        hide screen halter_2
    #minijeu
    label jeu_bouffe:
        scene fond_cuisine_jour with fade

        show image_theo_normal
        stop music
        play music "../audio/musique_cuisine.mp3"
        $ perso_theo("On doit faire une entrée", interact = False)
        $ result_9 = renpy.display_menu([ ("Oeuf mayo", "oeuf_mayo"), ("Soupe à la tomate", "soupe")])

        if result_9 == "oeuf_mayo":
            call screen show_oeuf
        if result_9 == "soupe":
            call screen show_tomate

    #labels oeuf mayo

    label Oeuf_Oeuf:
        perso_theo "C'est bien ! Il nous manque un ingrédient."
        call screen show_mayo

    label Oeuf_Viande:
        perso_theo "Dommage, je pense pas que l'on puisse faire un oeuf mayo avec ça..."
        call screen show_oeuf

    label Oeuf_Kiwi:
        perso_theo "Dommage, je pense pas que l'on puisse faire un oeuf mayo avec ça..."
        call screen show_oeuf

    label Mayo_Creme_Fraiche:
        perso_theo "Dommage, je ne pense pas que ce soit ça."
        call screen show_mayo

    label Mayo_Fromage:
        perso_theo "Hmm, je ne suis pas convaincu."
        call screen show_mayo

    label Mayo_Mayo:
        perso_theo "Super ! On a réussi à faire un oeuf mayo !"
        show oeuf_mayo

        pause(2)
        hide oeuf_mayo
        $ perso_theo("On doit faire un plat", interact = False)
        $ result_10 = renpy.display_menu([ ("Pâtes à la bolognaise", "pates_bolo"), ("Pâtes carbonara", "pates_carbo"), ("Burger", "burger")])
        if result_10 == "pates_bolo":
            call screen show_viande_bolo
        if result_10 == "pates_carbo":
            call screen show_lardons
        if result_10 == "burger":
            call screen show_pain

    #labels soupe tomate

    label Tomate_Tomate:
        perso_theo "C'est bien ! Il nous manque un ingrédient."
        call screen show_oignon

    label Tomate_Oeuf:
        perso_theo "Hmmm, je ne pense pas que ça soit le bon ingrédient."
        call screen show_tomate

    label Tomate_Lardons:
        perso_theo "Hmmm, je ne pense pas que ça soit le bon ingrédient."
        call screen show_tomate

    label Oignon_Oignon:
        perso_theo "Super ! On a réussi à faire une soupe à la tomate !"
        show soupe_tomate

        pause(2)
        hide soupe_tomate
        $ perso_theo("On doit faire un plat", interact = False)
        $ result_11 = renpy.display_menu([ ("Pâtes à la bolognaise", "pates_bolo"), ("Pâtes carbonara", "pates_carbo"), ("Burger", "burger")])
        if result_11 == "pates_bolo":
            call screen show_viande_bolo
        if result_11 == "pates_carbo":
            call screen show_lardons
        if result_11 == "burger":
            call screen show_pain

    label Oignon_Kiwi:
        perso_theo "Alors là, tu en fais exprès !"
        call screen show_oignon

    label Oignon_Chocolat:
        perso_theo "Du chocolat, vraiment ?"
        call screen show_oignon

    #labels pates bolo

    label Viande_Bolo_Viande:
        perso_theo "Déjà on a la viande, c'est un bon début !"
        call screen show_pates_bolo

    label Viande_Bolo_Sucre:
        perso_theo "On va peut-être éviter, c'est pas bon pour la ligne en plus !"
        call screen show_viande_bolo

    label Viande_Bolo_Pomme:
        perso_theo "On essaiera ça une prochaine fois."
        call screen show_viande_bolo

    label Pates_Bolo_Pates:
        perso_theo "On commence à avoir une bonne base avec ça !"
        call screen show_oignon_bolo

    label Pates_Bolo_Pain:
        perso_theo "C'est pas l'heure de faire des sandwichs !"
        call screen show_pates_bolo

    label Pates_Bolo_Pasteque:
        perso_theo "Oh non ça rend plein de flotte les pastèques..."
        call screen show_pates_bolo

    label Oignon_Bolo_Oignon:
        perso_theo "Ça va donner du goût !"
        call screen show_tomate_bolo

    label Oignon_Bolo_Pain:
        perso_theo "C'est pas l'heure de faire des sandwichs !"
        call screen show_oignon_bolo

    label Oignon_Bolo_Chocolat:
        perso_theo "Beurk !"
        call screen show_oignon_bolo

    label Tomate_Bolo_Tomate:
        perso_theo "Le clou du spectacle, la tomate ! Tout est prêt !"
        show pates_bolo

        pause(2)
        hide pates_bolo
        $ perso_theo("Il nous faut un dessert.", interact = False)
        $ result_12 = renpy.display_menu([ ("Mousse au chocolat", "mousse"), ("Salade de fruits", "salade")])
        if result_12 == "mousse":
            call screen show_chocolat
        if result_12 == "salade":
            call screen show_pomme

    label Tomate_Bolo_Sucre:
        perso_theo "Du sucre dans des pâtes carbo ?!"
        call screen show_tomate_bolo

    label Tomate_Bolo_Oeuf:
        perso_theo "Ça serait pas si mal mais il nous manque vraiment un ingrédient majeur."
        call screen show_tomate_bolo

    #labels pates carbo

    label Lardons_Lardons:
        perso_theo "Tout est bon dans le cochon !"
        call screen show_pates_carbo

    label Lardons_Chocolat:
        perso_theo "Des fois le sucré salé, c'est pas forcément bon tu sais ?"
        call screen show_lardons

    label Lardons_Pomme:
        perso_theo "Des fois le sucré salé, c'est pas forcément bon tu sais ?"
        call screen show_lardons

    label Pates_Carbo_Pates:
        perso_theo "On commence à avoir une bonne base avec ça !"
        call screen show_oignon_carbo

    label Pates_Carbo_Pain:
        perso_theo "C'est pas l'heure de faire des sandwichs !"
        call screen show_pates_carbo

    label Pates_Carbo_Kiwi:
        perso_theo "Original, mais non."
        call screen show_pates_carbo

    label Oignon_Carbo_Sucre:
        perso_theo "Des fois le sucré salé, c'est pas forcément bon tu sais ?"
        call screen show_oignon_carbo

    label Oignon_Carbo_Oignon:
        perso_theo "Ça va rajouter du goût !"
        call screen show_creme_fraiche

    label Oignon_Carbo_Pasteque:
        perso_theo "Oh non ça rend plein de flotte les pastèques !"
        call screen show_oignon_carbo

    label Creme_Fraiche_Creme_Fraiche:
        perso_theo "Miam, mets-y le paquet sur la crème fraîche !"
        show pates_carbo

        pause(2)
        hide pates_carbo
        $ perso_theo("Il nous faut un dessert.", interact = False)
        $ result_13 = renpy.display_menu([ ("Mousse au chocolat", "mousse"), ("Salade de fruits", "salade")])
        if result_13 == "mousse":
            call screen show_chocolat
        if result_13 == "salade":
            call screen show_pomme

    label Creme_Fraiche_Pain:
        perso_theo "C'est pas l'heure de faire des sandwichs !"
        call screen show_creme_fraiche

    label Creme_Fraiche_Chocolat:
        perso_theo "Du chocolat dans des pâtes carbo, j'aurais tout vu..."
        call screen show_creme_fraiche

    #labels burger

    label Pain_Pain:
        perso_theo "On a la base !"
        call screen show_viande_burger

    label Pain_Pates:
        perso_theo "Pas un grand fan de ce choix."
        call screen show_pain

    label Pain_Lardons:
        perso_theo "Pourquoi pas, mais on devrait déjà se munir de la base."
        call screen show_pain

    label Viande_Burger_Viande:
        perso_theo "Yes ! Un bon steak !"
        call screen show_tomate_burger

    label Viande_Burger_Oeuf:
        perso_theo "Tu veux pas mettre de la viande plutôt ?"
        call screen show_viande_burger

    label Viande_Burger_Kiwi:
        perso_theo "On va quand même pas mettre des kiwis dans nos burgers !"
        call screen show_viande_burger

    label Tomate_Burger_Tomate:
        perso_theo "Ça commence à ressembler à quelque chose !"
        call screen show_fromage

    label Tomate_Burger_Pomme:
        perso_theo "J'ai peur que ça gâche tout."
        call screen show_tomate_burger

    label Tomate_Burger_Creme_Fraiche:
        perso_theo "Je serais pas contre, mais y'en a plus !"
        call screen show_tomate_burger

    label Fromage_Fromage:
        perso_theo "Magnifique, bon appétit !"
        show burger

        pause(2)
        hide burger
        $ perso_theo("Il nous faut un dessert.", interact = False)
        $ result_14 = renpy.display_menu([ ("Mousse au chocolat", "mousse"), ("Salade de fruits", "salade")])
        if result_14 == "mousse":
            call screen show_chocolat
        if result_14 == "salade":
            call screen show_pomme

    label Fromage_Pates:
        perso_theo "Oh bah non, on va pas tout gâcher maintenant !"
        call screen show_fromage

    label Fromage_Pasteque:
        perso_theo "Mais non Zinédine, pas après tout ce que t'as fait !"
        call screen show_fromage

    #labels mousse au chocolat

    label Chocolat_Chocolat:
        perso_theo "C'est déjà un bon début !"
        call screen show_mousse_oeuf

    label Chocolat_Fromage:
        perso_theo "Bah non du coup !"
        call screen show_chocolat

    label Chocolat_Oignon:
        perso_theo "Je suis pas convaincu par cet ingrédient..."
        call screen show_chocolat

    label Oeuf_Mousse_Oeuf:
        perso_theo "Plus qu'un ingrédient et on est bons."
        call screen show_sucre

    label Oeuf_Mousse_Pates:
        perso_theo "Ça ne va vraiment pas ensemble..."
        call screen show_mousse_oeuf

    label Oeuf_Mousse_Tomate:
        perso_theo "Ça ne va vraiment pas ensemble..."
        call screen show_mousse_oeuf

    label Sucre_Sucre:
        perso_theo "C'est nickel !"
        show mousse
        pause(2)
        hide mousse
        jump suite_dessert
    label Sucre_Fromage:
        perso_theo "C'est honteux !"
        call screen show_sucre

    label Sucre_Pain:
        perso_theo "Je vois vraiment pas où tu veux en venir..."
        call screen show_sucre

    #labels salade de fruits

    label Pomme_Pomme:
        perso_theo "C'est un bon début."
        call screen show_kiwi

    label Pomme_Fromage:
        perso_theo "Alors pas du tout."
        call screen show_pomme

    label Pomme_Pain:
        perso_theo "Tu veux pas plutôt prendre un fruit ?"
        call screen show_pomme

    label Kiwi_Kiwi:
        perso_theo "Ça commence à ressembler à quelque chose !"
        call screen show_pasteque

    label Kiwi_Viande:
        perso_theo "Pas du tout."
        call screen show_kiwi

    label Kiwi_Creme_Fraiche:
        perso_theo "Je me demande bien ce que ça donnerait, mais non."
        call screen show_kiwi

    label Pasteque_Mayo:
        perso_theo "C'est dégueulasse."
        call screen show_pasteque

    label Pasteque_Oignon:
        perso_theo "C'est dégueulasse."
        call screen show_pasteque

    label Pasteque_Pasteque:
        perso_theo "Et voilà c'est prêt !"
        show salade

        pause(2)
        hide salade
    label suite_dessert:
    if result_8 == "un":
        hide image_theo_normal
        show image_alix_clin
        perso_alix "Ca y est ! On a fini !"
        perso_alix "C'était pas si dur finalement, enfin surtout parce que c'est toi qui as tout fait !"
        perso_alix "C'est un peu dommage car j'aurais bien voulu te voir te foirer"
        perso_joueur "Hein ? Comment ça ?"
        hide image_alix_clin
        show image_alix_sourire
        perso_alix "Mais non je rigole haha !"
        perso_alix "Allez dépêchons nous d'apporter les plats, je meurs de faim !"
        hide image_alix_sourire
    if result_8 == "deux":
        hide image_theo_normal
        show image_ema_sourire
        perso_ema "C'est pas trop tôt ! J'ai presque failli attendre."
        perso_joueur "Peut-être que si tu m'avais aidé aussi…"
        perso_ema "Mais non je voulais juste voir comment tu t'en sortais tout seul Bambi."
        perso_ema "Allez viens on doit emmener tout ça à table. ah moins que préfère qu'on se tire en emportant tout pour nous !"
        perso_joueur "Arrête de dire des bêtises..."
        hide image_ema_sourire
    if result_8 == "trois":
        hide image_theo_normal
        show image_rebecca_sourire
        perso_rebecca "Aaaah... on a enfin fini."
        perso_rebecca "C'était beaucoup plus fun que ce que je pensais"
        perso_joueur "Oui content qu'on est fini dans les temps."
        perso_rebecca "Bon on va passer à table maintenant ? Je t'aide à porter les plats."
        hide image_rebecca_sourire
    if result_8 == "quatre":
        show image_theo_normal
        perso_theo "Bien joué ! Tu t'es bien débrouillé ! Je vois que tu n'es pas un simple têtard. Mais…"
        hide image_theo_normal
        show image_theo_muscle
        perso_theo "Une vraie grenouille aux cuisses solides !!"
        perso_joueur "Oui ! Merci monsieur ! (Ce moniteur a beau être très particulier, c'est vraiment quelqu'un de sympa)"
        hide image_theo_muscle
        show image_theo_sourire
        perso_theo "Bon ce n'est pas tout ça mais tout les bons moment ont une fin !"
        perso_theo "Etre trop longtemps en contact avec mon corps de rêve pourrait bien finir par te faire perdre connaissance !"
        perso_theo "Il est donc important que tu te ménage ! Dépêche toi de rejoindre les autres !"
        hide image_theo_sourire

    scene fond_cantine_jour
    show fond_cantine_jour
    stop music
    play music "../audio/theme_global.mp3"
    hide image_theo_normal
    perso_joueur "(Etant liberé de mes occupations, je me dirige vers les tables pour manger)"
    perso_joueur "(Il n'y a plus de place nul part... à part une table de quatre vide. Je crois que je vais manger tout seul du coup...)"
    perso_joueur "(Tout d'un coup, les trois filles de ce matin se sont décidées à se mettre à coté de moi)"
    show image_ema_normal at left
    show image_rebecca_sourire at center
    show image_alix_normal at right
    perso_rebecca "C'est très bon ! C'est toujours meilleur quand c'est fait maison."
    perso_joueur "Oui, on a bien travaillé !"
    perso_ema "En tout cas, on peut dire que tu ne perds pas ton temps Anthony. Déjà autant de fille à ta table dès le premier jour ! Faut que tu me les présente !"
    perso_alix "Ah ouais t'es carrément comme Rebecca en fait !"
    hide image_rebecca_sourire
    show image_rebecca_gene at center
    perso_rebecca "Hein ?! Mais non !"
    perso_ema "C'est sérieux ?! Mais comment ça se fait que tu sois ici alors ?"
    perso_rebecca "C'est à dire que..."
    hide image_alix_normal
    show image_alix_sourire at right
    perso_alix "C'est ses parents qui l'ont envoyé ici! Elle aussi, elle est pas du genre à savoir s'amuser haha"
    perso_alix "D'ailleurs Anthony, si tu veux je peux t'apprendre tout ce qu'il faut savoir ici, ça te dit ?"
    hide image_ema_normal
    show image_ema_enerve at left
    perso_ema "Eh ! Baisse d'un ton tu veux ? Car tu t'y crois un peu trop si tu veux mon avis !"
    hide image_alix_sourire
    show image_alix_enerve at right
    perso_alix "Ah ouais vu comment t'es coincé, t'es pas mal non plus."
    perso_alix "Y'en as pas un pour rattraper l'autre. C'est à se demander ce que vous foutez dans une colo en forêt !"
    $ perso_rebecca ("Mais arrêtez ne vous disputez pas comme ça, c'est ridicule…", interact = False)
    $ result_15 = renpy.display_menu([ ("Ema a raison, je trouve que tu prend trop tes grand air Alix.", "un"), ("En vra, si Alix peut m'aider à pas m'ennuyer...","deux"), ("Laisse les, Rebecca...","trois"), ("(Sortir son téléphone pour afficher son désintérêt de la scène)","quatre")])
    if result_15 == "un":
        #affinité Ema +, Alix -
        $ affinite_ema += 10
        $ affinite_alix -= 10
        perso_alix "Pff... Si vous vous y mettez tout les deux, on peut plus rien faire de vous..."
        hide image_ema_enerve
        show image_ema_normal at left
        perso_ema "Bien dit Bambi ! On trouvera bien un moyen de s'éclater ici sans qu'on nous prenne de haut."
        perso_alix "Mais je vous prenais pas de haut ! Raaah laissez tombé !"
    if result_15 == "deux":
        #affinité Ema -, alix +
        $ affinite_ema -= 10
        $ affinite_alix += 10
        hide image_alix_enerve
        show image_alix_sourire at right
        perso_alix "Ah tu vois ? On dirait que même lui as compris !"
        perso_ema "Sérieux Bambi? Tu te range de son côté en plus !"
        perso_alix "Laisse la Anthony, on va bien s'amuser tout les deux tu va voir, Bambi"
    if result_15 == "trois":
        #affinité Rebecca +
        $ affinite_rebecca += 10
        hide image_rebecca_gene
        show image_rebecca_normal at center
        perso_rebecca "Ah oui ? Tu es sur"
        perso_joueur "Oui, Ema est toujours sur les nerfs de toute façon, désolé que tu dois assister à ça"
        hide image_rebecca_normal
        show image_rebecca_gene at center
        perso_rebecca "C'est pas grave je comprends..."
    if result_15 == "quatre":
        #affinité - tout le monde
        $ affinite_ema -= 10
        $ affinite_alix -= 10
        $ affinite_rebecca -= 10
        perso_ema "Et l'autre qui en as rien à foutre ! Je te rappelle qu'elle t'as critiqué Rebecca et toi !"
        hide image_rebecca_gene
        show image_rebecca_triste at center
        perso_rebecca "C'est rien c'est pas grave..."
        hide image_alix_enerve
        show image_alix_sourire at right
        perso_alix "Haha vous êtes tous trop bizarre..."
    perso_joueur "(On a fini le repas en vitesse pour éviter de rester trop longtemps dans cette ambiance pesante.)"
    perso_joueur "(Après avoir fini mon assiette, je pars directement dans ma chambre en disant au revoir à tout le monde.)"
    hide image_alix_sourire
    hide image_rebecca_triste
    hide image_rebecca_gene
    hide image_ema_normal



#Journal jour 1
    scene fond_journal
    show fond_journal

    if affinite_alix <= 40 and affinite_alix > 20 :
        perso_joueur "(Alix parle trop, elle m'énerve.)"
    if affinite_alix < 20 :
        perso_joueur "(Je déteste Alix.)"
    if affinite_alix >= 60 and affinite_alix < 80 :
        perso_joueur "(Alix a l'air sympa.)"
    if affinite_alix > 80 :
        perso_joueur "(J'aime vraiment beaucoup Alix.)"
    if affinite_ema <= 40 and affinite_ema > 20 :
        perso_joueur "(Ema a changée, elle m'agace.)"
    if affinite_ema < 20 :
        perso_joueur "(Je ne peux plus supporter Ema.)"
    if affinite_ema >= 60 and affinite_ema < 80 :
        perso_joueur "(Ema est toujours aussi sympa.)"
    if affinite_ema > 80 :
        perso_joueur "(Ema me plaît de plus en plus.)"
    if affinite_rebecca <= 40 and affinite_rebecca > 20 :
        perso_joueur "(Rebecca ne parle pas beaucoup, elle n'est pas intéressante.)"
    if affinite_rebecca < 20 :
        perso_joueur "(Rebecca ne sert à rien, elle ne parle jamais.)"
    if affinite_rebecca >= 60 and affinite_rebecca < 80 :
        perso_joueur "(J'aime bien Rebecca, elle a l'air sympa.)"
    if affinite_rebecca > 80 :
        perso_joueur "(Rebecca me plaît beaucoup, sa timidité la rend mignonne.)"



#Nuit
#Reveil du moniteur

    scene fond_noir
    perso_theo "DEBOUT MES GRENOUILLES !! IL EST DEJA 6H !"
    scene fond_chambre_matin with fade
    perso_joueur "(Il est déja 6h... j'ai envie de dormir moi)"
    perso_theo "Je vous laisse 10 minutes pour vous préparer, des CROOAA ssants... vous attendent à la cantine."
    perso_joueur "(Bon d'accord... si y'a des croissants, je veux bien...)"
    perso_joueur "(Allez, il est temps de se lever)"
    perso_joueur "(Faudrait que je vois des gens aussi aujourd'hui, que j'essaie un peu de m'integrer)"


#1er rdv Alix
    scene fond_couloir_jour
    show screen halter_9
    perso_joueur "(À peine sorti, je vois Alix me sauter directement dessus)"
    show image_alix_sourire
    $ perso_alix ("Hey, salut salut toi! T'as bien dormi? Ca roule ce matin?", interact = False)
    $ result_16 = renpy.display_menu([ ("Et ben, ca fait plaisir de voir quelqu'un d'aussi bonne humeur le matin", "un"), ("Ah euh... Salut... c'est quoi ton nom déja?","deux"), ("Oh doucement, pas dés le matin","trois")])
    if result_16 == "un":
        $affinite_alix += 10
        perso_joueur "(Eh ben, elle a l'air trés enthousiaste ce matin)"
        hide image_alix_sourire
        show image_alix_normal
        $ perso_alix ("Oh merci ! Souvent les gens veulent pas me parler aussi tôt, je sais pas pourquoi", interact = False)
        $ result_17 = renpy.display_menu([ ("Franchement, je vois pas pourquoi, moi je te trouve trop sympa ! J'aime bien t'écouter parler.", "quatre"), ("Je me demande bien pourquoi...","cinq")])
        if result_17 == "quatre":
            $ affinite_alix += 10
            hide image_alix_normal
            show image_alix_clin
            perso_alix "Ah ouai ! T'aimes bien quand je te parle ? Je vais te raconter ce que j'ai fais ce matin alors !!"
        if result_17 == "cinq":
            perso_alix "Bah ouai moi aussi je trouves ça étonnant ! Pourtant je suis normale, Regarde ce matin..."
    if result_16 == "deux":
        perso_alix "Ah tu te souviens pas ? Attends je te donne un indice, ça commence par un A. Allez, devine !!"
        $ perso_joueur ("(Est-ce que je lui répond franchement ?)", interact = False)
        $ result_18 = renpy.display_menu([ ("Alix ?", "alix"), ("Je sais pas moi Astérix ?","asterix"), ("Je sais pas moi Actarus ?","actarus"), ("Je sais pas moi Albator ?","albator")])
        if result_18 == "alix":
            $affinite_alix += 10
            hide image_alix_normal
            hide image_alix_clin
            show image_alix_sourire
            perso_alix "Ouais c'est ça, tu te souviens alors !"
            perso_alix "Tu m'impressionne ! La plupart des gens à qui j'adresse la parole se contente de m'ignorer d'habitude"
        if result_18 == "asterix" or result_18 == "actarus" or result_18 == "albator":
            hide image_alix_normal
            hide image_alix_clin
            show image_alix_sourire
            perso_alix "Ahah, j'ai la référence."
    if result_16 == "trois":
        $affinite_alix -= 10
        hide image_alix_sourire
        show image_alix_normal
        perso_alix "Quoi qu'est-ce qu'il y a ? T'as mal quelque part ? Tu veux que j'ailles te chercher un verre d'eau ?"
        perso_joueur "(Elle est bête ou juste bizarre?)"
        $ perso_joueur ("Non, c'est juste que...", interact = False)
        $ result_19 = renpy.display_menu([("Désolé, je suis pas très réveillé le matin.", "quatre"), ("Nan rien en fait...","cinq"), ("Tu me saoule dès le matin en fait...","six")])
        if result_19 == "quatre" or result_19 == "cinq":
            perso_joueur "Sinon ca va t..."
            perso_alix "Je me suis levée à 5 h. Ensuite, j'ai refais mon lit 3 fois, du coup il est très très très bien fait !!!"
            perso_alix "Ensuite, je voulais prendre l'air, du coup je suis sorti, j'ai vu un écureuil qui est monté dans un arbre."
            perso_alix "Du coup j'ai fais comme lui, parce que tu sais, moi je fais de l'escalade depuis que j'ai 6 ans, enfin 5..."
            perso_alix "Mais..... en fait je sais plus, mais j'adore ça ! Ensuite, je suis...."
            perso_joueur "(Elle parle vraiment beaucoup quand même.)"
            perso_theo "OH !!! LES GRENOUILLES ! VOS VENTRES DE TETARDS VONT PAS SE REMPLIR TOUT SEULS !"
            perso_theo "ON VA BIENTOT MANGER LES JEUNES !"
            hide image_alix_clin
            show image_alix_sourire
            perso_alix "Oh ouai je vais allez manger !! J'ai trop faim en plus !"
            perso_joueur "Elle devait vraiment avoir faim vù la vitesse à laquelle elle est partie !"
            hide image_alix_sourire
    if result_16 == "six":
        $affinite_alix -= 10
        perso_alix "(Je me suis barré sans la laisser finir)"
    hide screen halter_9
#1er rdv Ema
    scene fond_foret_jour
    show screen halter_3
    perso_joueur "(Aaaah, ca fait du bien de prendre un peu l'air aprés manger...)"
    perso_joueur "(Tiens, c'est pas Ema que je vois la bas?)"
    show image_ema_normal
    $ perso_ema ("Salut Bambi! Tu viens fumer avec moi?", interact = False)
    $ result_20 = renpy.display_menu([("Ouai grave. Tu me la paye Panpan?", "un"), ("Non, désolé je fume pas.","deux"), ("T'es tombée bien bas pour fumer...","trois")])
    if result_20 == "un":
        $affinite_ema += 10
        perso_joueur "(Ca fait lomgtemps que j'ai pas fumé)"
        perso_ema "Oh tu veux bien ? Je disais ça pour rigoler m.... Ah c'est pas vrai, j'ai plus de clope !!!"
        perso_ema "Bah t'inquiète, de toute façon, je sais que ça a jamais été ton truc"
        $ perso_ema ("Tu préfère qu'on aille se prendre un truc à la cantine ?", interact = False)
        $ result_21 = renpy.display_menu([("Ok, on y va!", "rien"), ("Pars devant, on se voit plus tard","nada")])
    if result_20 == "deux":
        $ perso_ema ("Ah ok, je pensais pas que tu étais autant coincé haha.", interact = False)
        $ result_22 = renpy.display_menu([("Hé arrête de me taquiner, propose moi autre chose que fumer c'est tout haha !", "quatre"), ("Bah excuse-moi mais fumer des joints c'est pas ma définition du fun. Allez salut...","cinq")])
        if result_22 == "quatre":
            $affinite_ema += 10
            perso_ema "Bah t'inquiète, de toute façon, je sais que ça a jamais été ton truc"
            $ perso_ema ("Tu préfère qu'on aille se prendre un truc à la cantine ?", interact = False)
            $ result_23 = renpy.display_menu([("Ok, on y va!", "rien"), ("Pars devant, on se voit plus tard","nada")])
        if result_22 == "cinq":
            $affinite_ema -= 10
            perso_ema "Hein?"
            perso_joueur "(Je fais demi tour sur mes deux talons... elle a vraiment changée depuis la derniere fois?)"
    if result_20 == "trois":
        $affinite_ema -= 10
        perso_ema "Hein?"
        perso_joueur "(Je fais demi tour sur mes deux talons... elle a vraiment changée depuis la derniere fois?)"
    hide image_ema_normal
    hide screen halter_3
#1er rdv rebecca
    label rdv_rebecca :

    scene fond_colo_jour
    show fond_colo_jour
    show screen halter_10

    perso_joueur "(Après le petit dej', j'avais envie de prendre un peu l'air, de profiter de la foret. Je m’assois alors sur un banc devant la mare aux grenouilles.)"
    perso_joueur "(Tiens? Quelqu'un s'approche de moi. Je reconnais ces cheveux. C'est Rebecca, la fille que j'ai rencontré hier.)"
    show image_rebecca_normal
    $ perso_rebecca ("Bon-bonjour, je peux m'assoir ici?", interact = False)
    $ result_24 = renpy.display_menu([ ("Oh tiens salut! Ouai ouai pas de souci, je te fais de la place", "un"), ("Ah oui, si tu veux","deux"), ("(Mentir) Ah désolé, j'attends quelqu'un.","trois")])
    if result_24 == "un" or result_24 == "deux":
        if result_24 == "un":
            $ affinite_rebecca += 10
        perso_joueur "(Je me décale sur le banc pour laisser une place à Rebecca. Elle s'assied à coté de moi)"
        $ perso_joueur ("(Le silence était pesant, il faut que je dise quelque chose et vite ou je vais mourir de géne)", interact = False)
        $ result_25 = renpy.display_menu([ ("Alors comment ca va? Quoi de beau? J'aimerai bien apprendre à te connaitre", "quatre"), ("Tu peux me parler tu sais, je mords pas","cinq"), ("Bah alors, parle moi un peu si tu veux...","six")])
        hide image_rebecca_normal
        if result_25 == "quatre":
            $ affinite_rebecca += 10
            show image_rebecca_blush
            perso_rebecca "Ah euuuh... c'est pas la grande forme... Mes parents m'ont forcée à venir ici pour me sociabiliser."
            hide image_rebecca_blush
            show image_rebecca_normal
            perso_rebecca "Ils trouvent que je me renferme trop sur moi-mème et que je ne parle pas assez..."
            hide image_rebecca_normal
            show image_rebecca_triste
            perso_rebecca "Mais c'est trop dur... j'ai du mal à m'exprimer"
            perso_joueur "Ah je comprends, j'étais comme ca avant... Sache que pour moi, y'a pas de problème."
            perso_joueur "Tu peux me parler quand tu veux, je ne mords pas"
            hide image_rebecca_triste
            show image_rebecca_sourire
            perso_rebecca "Ah merci..."
            perso_joueur "(Je continuais à parler pendant plusieurs minutes avec Rebecca.)"
            perso_joueur "(Je me rends compte que c'est quelqu'un de très sympa quand on sait l'aborder.)"
            perso_joueur "(Tout d'un coup, la voix du moniteur retentit dans toute la cour...)"
        if result_25 == "cinq":
            show image_rebecca_gene
            perso_rebecca "Ah euuuh... je suis pas trés bavarde moi d'habitude..."
            perso_joueur "Ah d'accord, pas de souci alors..."
            perso_joueur "(Un long silence pesant s'installa. Rebecca sort un livre et commence à le lire...)"
            perso_joueur "(Tout d'un coup, la voix du moniteur retentit dans toute la cour)"
        if result_25 == "six":
            $ affinite_rebecca -=10
            show image_rebecca_gene
            perso_rebecca "AAAaaaah je suis désolé, vraiment désolé..."
            hide image_rebecca_gene
            show image_rebecca_enerve
            perso_rebecca "Je-je... Je dois y aller"
            perso_joueur "Mais..."
            hide image_rebecca_enerve
            perso_joueur "Rebecca fait un demi tour sur ses talons et part en direction du dortoir"
            perso_joueur "Je crois que je l'ai vexée... Oh bon, c'est pas trés grave, j'ai le banc pour moi tout seul maintenant"
            perso_joueur "Tout d'un coup, la voix du moniteur retentit dans toute la cour."

    if result_24 == "trois":
        $ affinite_rebecca -=10
        hide image_rebecca_normal
        show image_rebecca_triste
        perso_rebecca "Ok... Pas de problème..."
        hide image_rebecca_triste
        perso_joueur "(Rebecca avait l'air déçue, comme si je lui avais piquer sa place. Elle commence à partir vers un autre banc.)"
        perso_joueur "(Mmmmh, tiens. Il y a quelque chose par terre... Une poupée?)"
        perso_joueur "(Ah oui! C'est la poupée de Rebecca, je l'ai vue avec, le premier jour.)"
        perso_joueur "(Il faut que je lui rende. Je me lève du banc et rattrape Rebecca par le bras.)"
        show image_rebecca_blush
        $ perso_joueur ("(Elle sursaute d'un coup et devient rouge comme une tomate.)", interact = False)
        $ result_26 = renpy.display_menu([ ("Ah! Excuse moi de te surprendre comme ça... Tiens, tu as fait tomber ta poupée. Elle a pris un peu la terre mais elle va bien", "quatre"), ("Excuse moi, tu as fait tomber ta poupée","cinq"), ("Tiens ton doudou, évite de le faire tomber la prochaine fois","six")])
        if result_26 == "quatre":
            $ affinite_rebecca += 10
            hide image_rebecca_blush
            show image_rebecca_gene
            perso_joueur "(Le visage de Rebecca semble alors s'apaiser... Comme si elle était rassuré par ma réponse)"
            perso_rebecca "Me-merci, c'est sympa de ta part..."
            perso_rebecca "Pa-par contre, est ce que tu peux me lacher le bras s'il te p-plait?..."
            perso_joueur "Oh pardon! Réflexe"
            hide image_rebecca_gene
            show image_rebecca_sourire
            perso_joueur "(Je lâche le bras de Rebecca et son visage esquisse alors un léger sourire tendre)"
            perso_joueur "De rien pour la poupée, c'est normal de rendre ce qui n'est pas à moi."
            hide image_rebecca_sourire
            show image_rebecca_blush
            perso_joueur "(Elle avait l'air très gênée depuis que je l'ai tenue par le bras. Elle n'ose pas croiser mon regard.)"
            perso_joueur "(L'ambiance pesante est tout d'un coup interrompue par un cri résonant dans toute la colo.)"
        if result_26 == "cinq":
            perso_rebecca "Me-merci mais est ce que tu peux me lacher s'il te plait..."
            perso_joueur "Oh pardon! Réflexe"
            hide image_rebecca_blush
            show image_rebecca_normal
            perso_joueur "(Je lâche le bras de Rebecca et elle semble s'apaiser un petit peu)"
            perso_joueur "(Elle reste de marbre face à moi, pas un mot, pas un sourire.)"
            perso_joueur "(L'ambiance pesante est tout d'un coup interrompue par un cri résonant dans toute la colo.)"
        if result_26 == "six":
            $ affinite_rebecca -= 10
            hide image_rebecca_blush
            show image_rebecca_enerve
            perso_rebecca "Me-merci..."
            perso_joueur "(Son visage se crispa, semblant énervé par la manière dont je l'aborde...)"
            perso_joueur "(Elle tire son bras en dehors de ma main brusquement et m'arrache la poupée de mes mains.)"
            perso_joueur "(Elle s'en va d'un pas rapide, me boudant complétement)"
            perso_joueur "(L'ambiance pesante est tout d'un coup interrompue par un cri résonant dans toute la colo.)"

    perso_theo "MES GRENOUILLES, ON S'ORGANISE UN MATCH DE TENNIS D'ENFER, VOUS VENEZ?!"
    perso_theo "NAN EN FAIT, C'EST PAS UNE QUESTION, VENEZ!"

    if result_24 == "quatre":
        perso_joueur "Allons y Rebecca, ça peut être drôle"
        hide image_rebecca_blush
        show image_rebecca_sourire
        perso_joueur "(Rebecca acquiesça avec un sourire tendre et me suivit jusqu'au terrain de tennis)"
    if result_24 == "cinq":
        perso_joueur "ON ARRIVE"
        hide image_rebecca_gene
        show image_rebecca_normal
        perso_joueur "(Je me lève du banc et commence à partir vers le terrain de tennis. Rebecca me suit juste aprés.)"
    if result_24 == "six":
        perso_joueur "(Trop bien un tennis! J'ai hâte de commencer !)"
        perso_joueur "(Je me lève du banc et commence à partir vers le terrain de tennis.)"
    hide image_rebecca_normal
    hide image_rebecca_sourire
    hide screen halter_10

# match de tennis (pong)

    scene fond_boom_jour
    show image_theo_normal
    perso_theo "Je suppose que tout le monde connait les regles du tennis? J'ai pas besoin de réexpliquer"
    perso_theo "Rebecca ! Tu as qu'a te mettre avec Anthony comme vous etes les derniers arrivés..."
    hide image_theo_normal
    show image_theo_sourire
    perso_theo "Allez, c'est parti! Faites bouger ces petites cuisses de grenouille"
    hide image_theo_sourire
    #Pong 1
    label pong_2_2:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False
    show fond_noir
    stop music
    play music "../audio/musique_pong.mp3"
    call screen pong

    $ quick_menu = True
    window show

    hide fond_noir
    show fond_boom_jour
    show image_theo_sourire

    perso_theo "Super match les grenouilles!"
    perso_theo "J'ai envie de jouer moi aussi! Qui veut m'affronter"
    hide image_theo_sourire
    show image_ema_enerve
    perso_ema "Non, moi ca ma saoule le tennis, j'aime pas ça... Je me casse"
    hide image_ema_enerve
    show image_theo_sourire
    perso_theo "Ah. Bon. Alors je vais affronter Anthony et Rebecca, c'est parti!"
    hide image_theo_sourire
    #Pong 2 version ALED

    label pong_theo:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False
    show fond_noir
    stop music
    play music "../audio/musique_pong.mp3"
    call screen pong_2

    $ quick_menu = True
    window show

    hide fond_noir*
    stop music
    play music "../audio/theme_global.mp3"
    show fond_boom_jour
    show image_theo_sourire
    perso_theo "Ah... ca fait du bien de se défouler comme ca une fois de temps en temps..."
    perso_theo "Vous pouvez disposer mes grenouilles favorites, on se revoit plus tard!"
    hide image_theo_sourire

    #faire choix de fille entre les trois
    label choix_date:

    $ perso_joueur ("Bon. Et si je profitais de mon temps libre pour passer du temps avec une des filles de la colo ?", interact = False)
    $ result_80 = renpy.display_menu([("Aller voir Ema", "un"), ("Aller voir Alix", "deux"), ("Allez voir Rebecca", "trois")])

# 2eme date Ema

    if result_80 == "un":
        scene fond_foret_jour
        show screen halter_4
        perso_joueur "(Pfiou, aprés ce match de tennis endiablé, je crois que je ne suis plus en mesure de faire quoi que ce soit)"
        perso_joueur "(Je vais rejoindre Ema pour discuter un peu avec elle, pour tuer le temps)"
        show image_ema_normal
        perso_joueur "Salut Ema! Tu fais quoi dehors?"
        if affinite_ema >= 50:
            perso_ema "Ah t'es là ! Je t'ai pas entendu arriver avec mon casque."
            $ perso_ema ("J'avais besoin de calme pour composer mon nouveau son. Tu veux l'écouter?", interact = False)
            $ result_27 = renpy.display_menu([ ("Ah ouai carrément! En plus je suis sùr que t'es super douée!", "un"), ("Nan, j'ai mal à la tête en ce moment... J'espere que ca te dérange pas Papan","deux")])
            if result_27 == "un":
                $affinite_ema += 10
                hide image_ema_normal
                show image_ema_sourire
                $ perso_ema ("Alors, t'aimes bien?", interact = False)
                $ result_28 = renpy.display_menu([ ("Ah mais c'est trop bien, t'as vraiment un talent pour la musique toi !", "trois"), ("C'est pas trop mon style désolé.","quatre")])
                if result_28 == "trois":
                    $affinite_ema += 10
                    perso_ema "Ah vraiment... ca te plait?"
                    perso_joueur "Ouai vraiment! Sinon ca te dirais qu'on se voit pour autre chose que de la musique ?"
                    hide image_ema_sourire
                    show image_ema_gene
                    perso_ema "Ah... Euuuhhh... baahh..."
                    perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                    perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
                if result_28 == "quatre":
                    $ affinite_ema -= 10
                    hide image_ema_sourire
                    show image_ema_triste
                    perso_ema "Ah..... pas grave alors, tu préférera peut-être quand il sera fini."
                    perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                    perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
            if result_27 == "deux":
                hide image_ema_normal
                show image_ema_triste
                perso_ema "Ah... Pas grave alors, tu préferera peut etre quand il sera fini"
                perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"

        if affinite_ema < 50:
            hide image_ema_normal
            show image_ema_enerve
            $ perso_ema ("Qu'est ce que tu me veux ?", interact = False)
            $ result_29 = renpy.display_menu([("Désolé je sais pas ce qui m'a pris, je pensais pas que ça t'affecterait autant.", "un"), ("J'aime tellement te faire chier, je ne peux pas m'en passer.","deux")])
            if result_29 == "un":
                $affinite_ema += 10
                perso_ema "Pense pas que ça va être si facile que je te pardonne."
                perso_joueur "Je suis encore désolé, je sais que j'ai trahi ta confiance et je m'en excuse encore."
                perso_joueur "Ca sera peut-être difficile qu'on redevienne amis mais on peut au moins essayer"
                perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
            if result_29 == "deux":
                $affinite_ema -= 10
                perso_ema "Tu te rends compte de ce que tu dis ?"
                perso_ema "T'es en train de briser une amitié qui dure depuis si longtemps en si peu de mots."
                $ perso_ema ("Réfléchis bien à la réponse que tu vas me donner : Est-ce vraiment ce que tu veux ?",interact = False)
                $ result_30 = renpy.display_menu([("Désolé je sais pas ce qui m'a pris, je pensais pas que ça t'affecterait autant.", "trois"), ("Mais tu te rends pas compte que je me fous de notre amitié.","quatre")])
                if result_30 == "trois":
                    $affinite_ema += 10
                    perso_ema "Pense pas que ça va être si facile que je te pardonne."
                    perso_joueur "Je suis encore désolé, je sais que j'ai trahi ta confiance et je m'en excuse encore."
                    perso_joueur "Ca sera peut-être difficile qu'on redevienne amis mais on peut au moins essayer"
                    perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                    perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
                if result_30 == "quatre":
                    $affinite_ema -= 20
                    perso_joueur "T'as totalement changé depuis qu'on se connait. Ce ne sera plus jamais comme avant."
                    perso_joueur "Allez, je me tire."
                    perso_joueur "(Dans un élan de colère, je fais demi tour sur mes talons, laissant Ema toute seule)"
    # 2 eme date Alix
    if result_80 == "deux" :
        scene fond_colo_jour
        show screen halter_4
        perso_joueur "(Pfiou, aprés ce match de tennis endiablé, je crois que je ne suis plus en mesure de faire quoi que ce soit)"
        perso_joueur "(Je vais rejoindre Alix pour discuter un peu avec elle, pour tuer le temps)"
        perso_joueur "Salut Alix! Tu veux discuter?"
        if affinite_alix >=50:
            show image_alix_sourire
            perso_alix "Ah super, je sais pas si tu savais mais j'adore discuter et surtout avec les gens que j'aime bien !"
            $ perso_alix ("Je t'ai déjà dit que je t'aimais bien ? Après moi j'aime bien tout le monde tu sais !", interact = False)
            $ result_31 = renpy.display_menu([ ("T'aime bien tout le monde  mais est-ce que tu as une préférence... ?", "un"), ("Ouais, moi aussi je trouve que t'es une super amie","deux")])
            if result_31 == "un":
                $affinite_alix += 10
                perso_alix "Ouai j'aime trop Rebecca !! Elle est vraiment trop sympa même si elle parle pas beaucoup."
                $ perso_alix ("En plus, elle n'est pas méchante avec moi, je peux lui parler pendant des heures, elle m'écoutera toujours.", interact = False)
                $ result_32 = renpy.display_menu([ ("T'as pas une autre personne dans ton cœur ?", "trois"), ("C'est vrai qu'elle est sympa...","quatre")])
                if result_32 == "trois":
                    $affinite_alix += 10
                    hide image_alix_sourire
                    show image_alix_gene
                    perso_alix "Euhhh..... je sais pas....qui j'aime...euhh... ah si, j'aime bien Théo..."
                    perso_alix "'Mais c'est vrai que y'a une personne que j'apprécie particulièrement dans cette colo et c'est t..."
                    perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                    perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
                if result_32 == "quatre":
                    perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                    perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                    perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
            if result_31 == "deux":
                hide image_alix_sourire
                show image_alix_normal
                perso_alix "Ah ok... cool alors."
                perso_alix "Tu veux qu'on parle de quoi ? Parce que tout à l'heure, j'ai un peu trop mangé mais du coup j'ai mal au ventre"
                perso_alix "Je peux plus monter en haut des sapins, je peux monter que aux chênes, et du coup j'ai plus la même vue et...."
                perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
        if affinite_alix < 50:
            show image_alix_enerve
            $ perso_alix ("Si c'est pour me dire que je suis soulante... tu peux repartir !", interact = False)
            $ result_33 = renpy.display_menu([ ("Désolé, j'étais pas dans mon assiette ces temps si, je suis juste venu pour parler.", "trois"), ("Ouai t'as raison je te trouve insupportable mais j'aime tellement te faire chier, je ne peux pas m'en passer...","quatre")])
            if result_33 == "trois":
                $affinite_alix += 10
                hide image_alix_enerve
                show image_alix_normal
                perso_alix "Ah ok... cool alors."
                perso_alix "Tu veux qu'on parle de quoi ? Parce que tout à l'heure, j'ai un peu trop mangé mais du coup j'ai mal au ventre"
                perso_alix "Je peux plus monter en haut des sapins, je peux monter que aux chênes, et du coup j'ai plus la même vue et...."
                perso_theo "HEY LES GRENOUILLES !! IL EST DEJA 20H ET JE VOUS RAPPELLE QU'ON DOIT ETRE COUCHÉ à 21H"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!!"
                perso_theo "EN PLUS, VOUS DEVEZ ETRE TRÉS FATIGUÉS APRES LE MATCH DE TENNIS !! TONI !!!! TRUANT !!!!"
                perso_joueur "(Ah! Je crois qu'il faut qu'on rentre...)"
            if result_33 == "quatre":
                $affinite_alix -= 20
                hide image_alix_enerve
                show image_alix_pleure
                perso_alix "Casse toi de là ! J'ai rien à te dire..."
                hide image_alix_pleure
                perso_joueur "(Je crois que je l'ai un peu enervé... Oh bon, c'est pas grave, elle s'en remettra."

# 2eme date Rebecca
    if result_80 == "trois":
        scene fond_colo_jour
        show fond_colo_jour
        show screen halter_4
        perso_joueur "(Pfiou, aprés ce match de tennis endiablé, je crois que je ne suis plus en mesure de faire quoi que ce soit)"
        perso_joueur "(Je vais rejoindre Rebecca pour discuter un peu avec elle, pour tuer le temps)"
        perso_joueur "(A cette heure la, elle doit sans doute etre à la cantine, en train de lire un livre)"
        scene fond_cantine_jour
        show image_rebecca_normal
        perso_joueur "Bingo! Trouvée!"
        hide image_rebecca_normal
        show image_rebecca_sourire
        $ perso_rebecca ("Oh bonjour Anthony, comment tu vas?", interact = False)
        $ result_34 = renpy.display_menu([ ("Mes jambes me tuent mais ça va. T'as été super forte au tennis, bravo.", "un"), ("Ca va et toi?","deux"), ("Ouai ouai ca va... j'en peux plus du tennis.","trois")])
        if result_34 == "un":
            $ affinite_rebecca += 10
            hide image_rebecca_sourire
            show image_rebecca_blush
            perso_rebecca "Merci, ça me fait plaisir."
            hide image_rebecca_blush
            show image_rebecca_sourire
            perso_rebecca "Pourtant, je ne fais pas beaucoup de sport habituellement... Je n'aime pas sortir."
            hide image_rebecca_sourire
            show image_rebecca_normal
            perso_rebecca "Mes parents m'ont souvent repris sur ca d'ailleurs... Ils ont peur que je me renferme sur moi mème pour le reste de ma vie"
            $ perso_rebecca ("Ils ont envie que je reussisse dans ma vie mais j'ai meme du mal à parler à ma poupée parfois", interact = False)
            $ result_35 = renpy.display_menu([ ("Moi je crois en toi, t'es quelqu'un de trés appréciable et tu progresse déja à la colo!", "quatre"), ("Ca doit pas être facile tout les jours dis donc...","cinq"), ("Peut etre essaye de te forcer à sortir... Ca peut aider","six")])
            if result_35 == "quatre":
                $ affinite_rebecca += 10
                hide image_rebecca_normal
                show image_rebecca_sourire
                perso_rebecca "Tu le pense vraiment?"
                perso_joueur "Oui, bien sur. Tu es quelqu'un de trés sympatique. Je suis sur que tu peux y arriver"
                hide image_rebecca_sourire
                show image_rebecca_blush
                perso_rebecca "D'accord, si tu le dis."
                perso_rebecca "Depuis qu'on a déménagé avec mes parents, j'ai perdu tous mes amis... J'espere pouvoir en retrouver un avec toi"
                perso_joueur "On ne l'est pas déja?"
                perso_rebecca "..."
                hide image_rebecca_blush
                show image_rebecca_sourire
                perso_rebecca "Me-merci beaucoup."

            if result_35 == "cinq":
                perso_rebecca "Je suis comme ca, je fais avec..."
                perso_rebecca "J'ai toujours été comme ca depuis que j'ai déménagé. J'ai perdu tout mes amis et maintenant je n'ose plus adresser la parole"
                perso_joueur "Hesite pas, faut parler pour se faire des amis, c'est la dure loi de l'amitié"
                hide image_rebecca_normal
                show image_rebecca_gene
                perso_rebecca "Ou-oui"
            if result_35 == "six":
                $affinite_rebecca -= 10
                hide image_rebecca_normal
                show image_rebecca_enerve
                perso_rebecca "Mais j-j'essaye m-mais je n'y arrive pas..."
                perso_joueur "Et bien il faut te forcer..."
                perso_rebecca "M-mais..."
                hide image_rebecca_enerve
                perso_joueur "(Rebecca part en pleurs et en courant, claquant la porte de la cantine derriere elle.)"
                perso_joueur "(Boh, au moins elle apprendra à la dure... Je devrais peut etre attendre ici pour manger maintenant)"


        if result_34 == "deux":
            hide image_rebecca_sourire
            show image_rebecca_normal
            perso_rebecca "Oh moi, ca pourrait mieux aller... Le sport m'a completement lessivée"
            perso_rebecca "Je suis nulle en sports, vu que d'habitude, je ne sors quasiment pas"
            hide image_rebecca_normal
            show image_rebecca_triste
            $ perso_rebecca ("Je m'enferme dans ma chambre... L'interaction humaine me mets mal à l'aise et cette colo n'arrange rien", interact = False)
            $ result_36 = renpy.display_menu([ ("Mais non! Tu te débrouille trés bien! Tu t'amuse dans cette colo non?", "quatre"), ("Ouah, ca doit pas etre facile tout les jours","cinq"), ("Eh beh, il faut sortir un peu une fois de temps en temps","six")])
            if result_36 == "quatre":
                $ affinite_rebecca += 10
                hide image_rebecca_triste
                show image_rebecca_sourire
                perso_rebecca "Tu le pense vraiment?"
                perso_joueur "Oui, bien sur. Je trouve que tu es quelqu'un de trés sympatique. Et les autres t'apprécient beaucoup aussi"
                hide image_rebecca_sourire
                show image_rebecca_blush
                perso_rebecca "D'accord, si tu le dis."
                perso_rebecca "Depuis qu'on a déménagé avec mes parents, j'ai perdu tous mes amis... J'espere pouvoir en retrouver un avec toi"
                perso_joueur "On ne l'est pas déja?"
                perso_rebecca "..."
                hide image_rebecca_blush
                show image_rebecca_sourire
                perso_rebecca "Me-merci beaucoup."
                scene fond_noir
                perso_joueur "(Je passe quelques temps avec Rebecca avant d'aller manger)"
            if result_36 == "cinq":
                hide image_rebecca_triste
                show image_rebecca_normal
                perso_rebecca "Je suis comme ca, je fais avec..."
                perso_rebecca "J'ai toujours été comme ca depuis que j'ai déménagé. J'ai perdu tout mes amis et maintenant je n'ose plus adresser la parole"
                perso_joueur "Hesite pas, faut parler pour se faire des amis, c'est la dure loi de l'amitié"
                hide image_rebecca_normal
                show image_rebecca_gene
                perso_rebecca "Ou-oui"
                perso_joueur "(Rebecca remets le nez dans son livre, tandis que moi je reste planté la, en attendant le repas)"
            if result_36 == "six":
                $ affinite_rebecca -= 10
                hide image_rebecca_triste
                show image_rebecca_enerve
                perso_rebecca "Pou-pourquoi tu es mechant comme ca, tu m'enerve..."
                perso_joueur "(D'un coup, dans une crise de colère, Rebecca leve sa main et me claque sur la joue d'une violence inattendue)"
                hide image_rebecca_enerve
                perso_joueur "(Rebecca part en pleurs et en courant, claquant la porte de la cantine derriere elle.)"
                perso_joueur "(Boh, au moins elle apprendra à la dure... Je devrais peut etre attendre ici pour manger maintenant)"
        if result_34 == "trois":
            hide image_rebecca_sourire
            show image_rebecca_normal
            perso_rebecca "Ah d'accord... C'est vrai que c'est fatiguant"
            perso_joueur "Oh que oui..."
            perso_rebecca "Euuuuhhh..."
            $ perso_joueur ("(Je devrais peut etre dire quelque chose... C'est trop calme, j'aime pas beaucoup ca)", interact = False)
            $ result_37 = renpy.display_menu([ ("T'as pas l'air trés en forme... Quelque chose ne va pas?", "quatre"), ("... (Je sais pas quoi dire!)","cinq"), ("Et sinon, tu t'habille normalement quelques fois? Ca doit pas aider socialement","six")])
            if result_37 == "quatre":
                hide image_rebecca_normal
                show image_rebecca_enerve
                perso_rebecca "Non... enfin si... Lai-laisse moi tranquille..."
                perso_joueur "Mais j'essaie juste de t'aider..."
                hide image_rebecca_enerve
                perso_joueur "(Rebecca se retourne et semble ne plus vouloir me parler...)"
                perso_joueur "(Elle remet le nez dans son livre, tandis que moi je reste planté la, en attendant le repas)"
            if result_37 == "cinq":
                perso_rebecca "..."
                perso_joueur "(La situation est trés malaisante, nous sommes tous les deux dans la cantine sans rien se dire...)"
                perso_joueur "(Je vais rester planté jusqu'à ce que le repas arrive...)"
            if result_37 == "six":
                $ affinite_rebecca -= 10
                hide image_rebecca_normal
                show image_rebecca_enerve
                perso_rebecca "Mais ce sont mes habits normaux... C'est vraiment pas sympa de me dire ca franchement..."
                perso_joueur "(D'un coup, dans une crise de colère, Rebecca leve sa main et me claque sur la joue d'une violence inattendue)"
                hide image_rebecca_enerve
                perso_joueur "(Rebecca part en pleurs et en courant, claquant la porte de la cantine derriere elle.)"
                perso_joueur "(Boh, au moins elle apprendra à la dure... Je devrais peut etre attendre ici pour manger maintenant)"

    hide screen halter_4

#action ou verite
    label action_verite:

    scene fond_chambre_nuit
    show fond_chambre_nuit
    show screen halter_5

    if (affinite_alix > affinite_rebecca and affinite_alix > affinite_ema):
        show image_alix_normal
        perso_alix "Ah t'es là, avec les filles on allait commencer un jeu, je ne sais pas si tu connais, ça s'appelle “action ou vérité”."
        hide image_alix_normal
        show image_alix_sourire
        perso_alix "Personellement, je prends souvent action, mais c'est parce que j'arrive pas à rester en place."
        hide image_alix_sourire
        show image_alix_clin
        $ perso_alix("Et toi alors, tu veux jouer ?", interact = False)
        $ result_38 = renpy.display_menu([("Ah ouais, carrément ! J'adore ce genre de jeu !", "un"), ("Désolé mais je suis un peu fatigué, je vais aller dormir", "deux")])
        if result_38 == "un":
            perso_joueur "(Elle m'emmène dans la chambre et je vois déjà les deux autres filles qui m'attendent avec le jeu déjà sorti.)"
            perso_joueur "(On s'apprête à commencer de jouer lorsque Théo surgit de nulle part !)"
            hide image_alix_clin
            show image_theo_sourire
            perso_theo "Alors les jeunes ! On fait trop de bruit par ici ?!"
            hide image_theo_sourire
            show image_theo_normal
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Le jeu va enfin pouvoir commencer mais avec Théo et je pense que l'on va bien rigoler avec lui dans la partie.)"
            jump suite_action_verite
        if result_38 == "deux":
            perso_joueur "Désolé mais je suis un peu fatigué, je vais aller dormir."
            hide image_alix_clin
            perso_joueur "(Je croise Théo sur le chemin du dortoir, il s'approche pour me parler.)"
            show image_theo_normal
            perso_theo "Salut ma petite rainette ! Ton séjour se passe bien ? Tu arrives bien à t'intégrer ?"
            perso_joueur "Oui tout va bien, je suis juste un peu fatigué, je pense que je... (vous êtes coupés par des rires qui se font entendre depuis la chambre des filles)"
            perso_theo "Vient avec moi ma grenouilette ! Nous allons voir pourquoi les filles rigolent plus fort que des grenouilles Croas !"
            perso_joueur "(Je suis donc Théo, mais une fois arrivé dans le dortoir des filles, son regard change complètement !)"
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Je me retrouve contraint de jouer, cela dit, avec Théo, le jeu risque d'être amusant.)"
            jump suite_action_verite

    if (affinite_rebecca >= affinite_alix and affinite_rebecca >= affinite_ema):
        show image_rebecca_normal
        $ perso_rebecca("B-Bonsoir... Ça te dit de faire un verit... euh... non... un “action ou vérité” avec les filles ?", interact = False)
        $ result_39 = renpy.display_menu([("Ah ouais, carrément ! J'adore ce genre de jeu !", "un"), ("Désolé mais je suis un peu fatigué, je vais aller dormir", "deux")])
        if result_39 == "un":
            perso_joueur "(Elle m'emmène dans la chambre et je vois déjà les deux autres filles qui m'attendent avec le jeu déjà sorti.)"
            perso_joueur "(On s'apprête à commencer de jouer lorsque Théo surgit de nulle part !)"
            hide image_rebecca_normal
            show image_theo_sourire
            perso_theo "Alors les jeunes ! On fait trop de bruit par ici ?!"
            hide image_theo_sourire
            show image_theo_normal
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Le jeu va enfin pouvoir commencer mais avec Théo et je pense que l'on va bien rigoler avec lui dans la partie.)"
            jump suite_action_verite
        if result_39 == "deux":
            perso_joueur "Désolé mais je suis un peu fatigué, je vais aller dormir."
            hide image_rebecca_normal
            perso_joueur "(Je croise Théo sur le chemin du dortoir, il s'approche pour me parler.)"
            show image_theo_normal
            perso_theo "Salut ma petite rainette ! Ton séjour se passe bien ? Tu arrives bien à t'intégrer ?"
            perso_joueur "Oui tout va bien, je suis juste un peu fatigué, je pense que je... (vous êtes coupés par des rires qui se font entendre depuis la chambre des filles)"
            perso_theo "Vient avec moi ma grenouilette ! Nous allons voir pourquoi les filles rigolent plus fort que des grenouilles Croas !"
            perso_joueur "(Je suis donc Théo, mais une fois arrivé dans le dortoir des filles, son regard change complètement !)"
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Je me retrouve contraint de jouer, cela dit, avec Théo, le jeu risque d'être amusant.)"
            jump suite_action_verite

    if (affinite_ema > affinite_rebecca and affinite_ema > affinite_alix):
        show image_ema_normal
        perso_ema "Hey ! Les filles m'ont proposé de faire un “action ou vérité” et vu que t'es là, ça te dit de nous rejoindre ?"
        $ result_40 = renpy.display_menu([("Ah ouai, carrément J'adore ce genre de jeu !", "un"), ("Désolé mais je suis un peu fatigué, je vais aller dormir", "deux")])
        if result_40 == "un":
            perso_joueur "(Elle m'emmène dans la chambre et je vois déjà les deux autres filles qui m'attendent avec le jeu déjà sorti.)"
            perso_joueur "(On s'apprête à commencer de jouer lorsque Théo surgit de nulle part !)"
            hide image_ema_normal
            show image_theo_sourire
            perso_theo "Alors les jeunes ! On fait trop de bruit par ici ?!"
            hide image_theo_sourire
            show image_theo_normal
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Le jeu va enfin pouvoir commencer mais avec Théo et je pense que l'on va bien rigoler avec lui dans la partie.)"
            jump suite_action_verite
        if result_40 == "deux":
            perso_joueur "Désolé mais je suis un peu fatigué, je vais aller dormir."
            hide image_ema_normal
            perso_joueur "(Je croise Théo sur le chemin du dortoir, il s'approche pour me parler.)"
            show image_theo_normal
            perso_theo "Salut ma petite rainette ! Ton séjour se passe bien ? Tu arrives bien à t'intégrer ?"
            perso_joueur "Oui tout va bien, je suis juste un peu fatigué, je pense que je... (vous êtes coupés par des rires qui se font entendre depuis la chambre des filles)"
            perso_theo "Vient avec moi ma grenouilette ! Nous allons voir pourquoi les filles rigolent plus fort que des grenouilles Croas !"
            perso_joueur "(Je suis donc Théo, mais une fois arrivé dans le dortoir des filles, son regard change complètement !)"
            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
            hide image_theo_normal
            show image_theo_muscle
            perso_theo "SANS MOI ?!"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
            perso_joueur "(Je me retrouve contraint de jouer, cela dit, avec Théo, le jeu risque d'être amusant.)"
            jump suite_action_verite
#    else:
#        show image_rebecca_normal
#        $ perso_rebecca("B-Bonsoir... Ça te dit de faire un verit... euh... non... un “action ou vérité” avec les filles ?", interact = False)
#        $ result_41 = renpy.display_menu([("Ah ouais, carrément ! J'adore ce genre de jeu !", "un"), ("Désolé mais je suis un peu fatigué, je vais aller dormir", "deux")])
#        if result_41 == "un":
#            perso_joueur "(Elle m'emmène dans la chambre et je vois déjà les deux autres filles qui m'attendent avec le jeu déjà sorti.)"
#            perso_joueur "(On s'apprête à commencer de jouer lorsque Théo surgit de nulle part !)"
#            hide image_rebecca_normal
#            show image_theo_sourire
#            perso_theo "Alors les jeunes ! On fait trop de bruit par ici ?!"
#            hide image_theo_sourire
#            show image_theo_normal
#            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
#            hide image_theo_normal
#            show image_theo_muscle
#            perso_theo "SANS MOI ?!"
#            hide image_theo_muscle
#            show image_theo_muscle_inverse
#            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
#            perso_joueur "(Le jeu va enfin pouvoir commencer mais avec Théo et je pense que l'on va bien rigoler avec lui dans la partie.)"
#            jump suite_action_verite
#        if result_41 == "deux":
#            perso_joueur "Désolé mais je suis un peu fatigué, je vais aller dormir."
#            hide image_ema_normal
#            perso_joueur "(Je croise Théo sur le chemin du dortoir, il s'approche pour me parler.)"
#            show image_theo_normal
#            perso_theo "Salut ma petite rainette ! Ton séjour se passe bien ? Tu arrives bien à t'intégrer ?"
#            perso_joueur "Oui tout va bien, je suis juste un peu fatigué, je pense que je... (vous êtes coupés par des rires qui se font entendre depuis la chambre des filles)"
#            perso_theo "Vient avec moi ma grenouilette ! Nous allons voir pourquoi les filles rigolent plus fort que des grenouilles Croas !"
#            perso_joueur "(Je suis donc Théo, mais une fois arrivé dans le dortoir des filles, son regard change complètement !)"
#            perso_theo "Oh mais, ne me dites pas que vous avez commencé un “action ou vérité” !"
#            hide image_theo_normal
#            show image_theo_muscle
#            perso_theo "SANS MOI ?!"
#            hide image_theo_muscle
#            show image_theo_muscle_inverse
#            perso_theo "Après un tel affront, vous allez devoir accepter que je vous rejoigne !"
#            perso_joueur "(Je me retrouve contraint de jouer, cela dit, avec Théo, le jeu risque d'être amusant.)"
#            jump suite_action_verite

        label suite_action_verite :
            perso_joueur "(Théo m'attrape par le bras pour que je sois à côté de lui. Me voilà donc entre Mr. Muscle et Rebecca.)"
            hide image_theo_muscle_inverse
            show image_theo_normal
            perso_theo "Les règles sont simples, une personne choisit “action” ou “vérité”, puis je lis la carte correspondante. Une fois le défi réalisé, on passe au suivant."
            hide image_theo_normal
            show image_theo_sourire
            perso_theo "Alors je commence pour donner l'exemple ! Je choisis action !"
            perso_joueur "(La carte indique : “faites dix pompes”.)"
            hide image_theo_sourire
            show image_theo_muscle
            perso_theo "C'est pas assez ! J'en fait 110 !"
            hide image_theo_muscle
            show image_theo_muscle_inverse
            perso_theo "Et pour ce défi je vais devoir croire en l'âme de mes muscles ! BANG BANG"
            perso_joueur "(J'ai rarement vu quelqu'un faire des pompes aussi vite !)"
            hide image_theo_muscle_inverse
            show image_theo_sourire
            perso_theo "Quinze secondes trop chrono ! J'ai battu mon record !"
            hide image_theo_sourire
            show image_theo_muscle
            perso_theo "Regardez mes muscles !"
            hide image_theo_muscle
            show image_theo_normal
            perso_theo "Le joueur suivant est Alix !"
            hide image_theo_normal
            show image_alix_normal
            perso_alix "Je sais pas... J'hésite, je suis un peu fatiguée avec le match de tennis d'aujourd'hui..."
            hide image_alix_normal
            show image_theo_normal
            perso_theo "Et bien tu peux prendre une carte action, au moins tu seras sûre de bien dormir ce soir !"
            perso_joueur "(La carte indique : “En 20 secondes, gagnez le plus de hauteur possible.”)"
            hide image_theo_normal
            show image_ema_enerve
            perso_ema "Hey ! Mais pourquoi tu me pousses comme ça ?!"
            perso_ema "Et pourquoi tu ouvres la fenêtre ?!"
            hide image_ema_enerve
            show image_alix_sourire
            perso_alix "Je vais grimper un arbre !"
            hide image_alix_sourire
            show image_rebecca_gene
            perso_rebecca "Reviens Alix ! Fais attention, tu vas te faire mal..."
            hide image_rebecca_gene
            show image_alix_sourire
            perso_alix "Ça y est ! Je suis en haut !"
            hide image_alix_sourire
            show image_theo_sourire
            perso_theo "En seulement 15 secondes ! Mais tu ne serais pas ma fille par hasard ?!"
            hide image_theo_sourire
            show image_ema_normal
            perso_ema "Mais vous êtes vraiment tous tarés ici..."
            hide image_ema_normal
            show image_alix_clin
            perso_alix "Je suis peut-être tarée mais en attendant, c'est à toi de choisir entre “action” et “vérité” !"
            hide image_alix_clin
            show image_ema_normal
            perso_ema "Je suis trop fatiguée pour choisir “action”, je choisis “vérité”."
            hide image_ema_normal
            show image_theo_normal
            perso_theo "C'est parti pour une carte “vérité” !"
            perso_joueur "(La carte indique : “Quel est votre plus grand défaut ?”)"
            hide image_theo_normal
            show image_ema_normal
            perso_ema "Moi ? J'ai pas de défauts !"
            hide image_ema_normal
            show image_alix_enerve
            perso_alix "Bien sûr que si ! Tu n'es pas marrante et tu t'énerves facilement. Tu devrais prendre exemple sur Rebecca, elle au moins, elle ne s'énerve pas !"
            hide image_alix_enerve
            show image_rebecca_gene
            perso_rebecca "Ah... C'est gentil... Enfin je crois..."
            hide image_rebecca_gene
            show image_ema_enerve
            perso_ema "Mais t'es vraiment insupportable Alix ! Cette fille n'arrête tellement pas de parler qu'on entend qu'elle ! Regardez, elle ne m'écoute même pas !"
            hide image_ema_enerve
            show image_ema_normal
            perso_ema "Bon d'accord, je veux bien admettre que je m'énerve facilement mais de là à dire que je n'ai pas d'humour..."
            perso_ema "Bon allez, à ton tour Rebecca"
            hide image_ema_normal
            show image_rebecca_gene
            perso_rebecca "Et bien... Je pense que je vais prendre acti... hm non plutôt vérité."
            hide image_rebecca_gene
            show image_theo_normal
            perso_theo "Ok, je pioche une carte “vérité” !"
            perso_joueur "(La carte indique : “Quelle est ta plus grande qualité ?”)"
            hide image_theo_normal
            show image_rebecca_gene
            perso_rebecca "Euh... Je sais pas..."
            hide image_rebecca_gene
            show image_alix_sourire
            perso_alix "Mais si ! C'est simple de se trouver des qualités ! Moi, je suis super dynamique, j'aime la nature, la musique et toi tu es calme, c'est ça ta qualité !"
            hide image_alix_sourire
            show image_rebecca_gene
            perso_rebecca "Ah... On va dire que je  suis calme alors..."
            hide image_rebecca_gene
            show image_theo_normal
            $ perso_theo("Bon, maintenant au tour de Anthony", interact = False)
            $ result_42 = renpy.display_menu([("Je choisis “action”", "un"), ("Je choisis “vérité”", "deux")])
            if result_42 == "un":
                perso_theo "C'est parti pour une action !"
                perso_joueur "(La carte indique : “Embrassez quelqu'un.”)"
                hide image_theo_normal
                $ perso_joueur ("(Qui vais-je choisir ?)", interact = False)
                $ result_60 = renpy.display_menu([("Choisir Alix", "un"), ("Choisir Rebecca", "deux"), ("Choisir Ema", "trois"), ("Choisir Théo", "quatre")])
                if result_60 == "un":
                    if (affinite_alix >= 60):
                        show image_alix_gene
                        perso_alix "Moi ? Vraiment ? Ça me gêne un peu..."
                    if (affinite_alix <= 20):
                        show image_alix_enerve
                        perso_alix "T'approche pas de moi ! Ne me parle même pas !"
                if result_60 == "deux":
                    if (affinite_rebecca >= 60):
                        show image_rebecca_blush
                        perso_rebecca "Euh... m-merci, mais tu n'es pas obligé... Enfin je t'aimes b-bien aussi mais ça me gêne un peu..."
                    if (affinite_rebecca <= 20):
                        show image_rebecca_enerve
                        perso_rebecca "Ah... Désolé mais je ne veux pas."
                if result_60 == "trois":
                    if (affinite_ema >= 60 and affinite_rebecca < 60 and affinite_alix < 60):
                        show image_ema_gene
                        perso_ema "Oh tu me choisis moi ? Ça me touche vraiment."
                    if (affinite_ema <= 20):
                        show image_ema_enerve
                        perso_ema "T'approche pas sinon tes dents vont finir dans le parquet."
                if result_60 == "quatre":
                    show image_theo_blush
                    perso_theo "Allez, viens me faire un bisou !"
            if result_42 == "deux":
                perso_theo "C'est parti pour vérité !"
                $ perso_joueur ("(La carte indique : “Quelle est la personne que vous appréciez le plus dans cette salle ?.”)", interact = False)
                $ result_61 = renpy.display_menu([("Choisir Alix", "un"), ("Choisir Rebecca", "deux"), ("Choisir Ema", "trois"), ("Choisir Théo", "quatre")])
                if result_61 == "un":
                    if affinite_alix >= 60 :
                        hide image_theo_normal
                        show image_alix_gene
                        perso_alix "Moi ? Vraiment ? Ça me gêne un peu..."
                    if affinite_alix <= 20 :
                        hide image_theo_normal
                        show image_alix_enerve
                        perso_alix "Mais bien sûr ! Pff..."
                if result_61 == "deux":
                    if (affinite_rebecca >= 60):
                        hide image_theo_normal
                        show image_rebecca_blush
                        perso_rebecca "Euh... m-merci, mais tu n'es pas obligé... Enfin je t'aimes b-bien aussi mais ça me gêne un peu..."
                    if (affinite_rebecca <= 20):
                        hide image_theo_normal
                        show image_rebecca_enerve
                        perso_rebecca "Euh... D'accord..."
                if result_61 == "trois":
                    if affinite_ema >= 60 :
                        hide image_theo_normal
                        show image_ema_gene
                        perso_ema "Oh tu me choisis moi ? Ça me touche vraiment."
                    if affinite_ema <= 20:
                        hide image_theo_normal
                        show image_ema_enerve
                        perso_ema "Fait pas genre... T'as changé..."
                if result_61 == "quatre":
                    hide image_theo_normal
                    show image_theo_blush
                    perso_theo "Oh c'est trop mignon ! Viens me faire un câlin !"

            hide image_alix_gene
            hide image_rebecca_blush
            hide image_ema_gene
            hide image_rebecca_enerve
            hide image_alix_enerve
            hide image_ema_enerve
            hide image_theo_blush
            show image_theo_normal
            perso_theo "Il est déjà 21h05, c'est terrible ! On doit aller se coucher maintenant sinon on ne va pas être en forme pour demain !"
    hide screen halter_5
#Journal jour 2
    scene fond_journal
    show fond_journal

    if (affinite_alix <= 40 and affinite_alix > 20) :
        perso_joueur "(Alix parle trop, elle m'énerve.)"
    if (affinite_alix < 20) :
        perso_joueur "(Je déteste Alix.)"
    if (affinite_alix >= 60 and affinite_alix < 80) :
        perso_joueur "(Alix a l'air sympa.)"
    if (affinite_alix > 80) :
        perso_joueur "(J'aime vraiment beaucoup Alix.)"
    if (affinite_ema <= 40 and affinite_ema > 20) :
        perso_joueur "(Ema a changée, elle m'agace.)"
    if (affinite_ema < 20) :
        perso_joueur "(Je ne peux plus supporter Ema.)"
    if (affinite_ema >= 60 and affinite_ema < 80) :
        perso_joueur "(Ema est toujours aussi sympa.)"
    if (affinite_ema > 80) :
        perso_joueur "(Ema me plaît de plus en plus.)"
    if (affinite_rebecca <= 40 and affinite_rebecca > 20) :
        perso_joueur "(Rebecca ne parle pas beaucoup, elle n'est pas intéressante.)"
    if (affinite_rebecca < 20) :
        perso_joueur "(Rebecca ne sert à rien, elle ne parle jamais.)"
    if (affinite_rebecca >= 60 and affinite_rebecca < 80) :
        perso_joueur "(J'aime bien Rebecca, elle a l'air sympa.)"
    if (affinite_rebecca > 80) :
        perso_joueur "(Rebecca me plaît beaucoup, sa timidité la rend mignonne.)"

    scene fond_noir
    perso_theo "Allez debout !!! On a une grosse journée aujourd'hui !"
    scene fond_chambre_matin with fade
    perso_theo "Venez me retrouver à l'extérieur quand vous aurez fini de vous préparer !"
    perso_joueur "(Tiens? Je me demande pourquoi il veut nous voir)"
    perso_joueur "(Je sors de mon lit et je me prépare à partir rapido)"

    scene fond_colo_matin
    perso_theo "Bon alors, mes p'tites grenouilles ! Ce soir, on laisse place à la dance, on fait une boum !"
    perso_theo "Mais va falloir la préparer, alors on va faire des groupes de 2 et on va travailler dur !"
    #choix de la meuf (que si > 50 d'affinitée)

    scene fond_boom_jour
    show screen halter_6
    perso_joueur "(On etait tous en train de préparer la boom pour ce soir. On veut tous en faire une super fête.)"
    perso_joueur "(Tout d'un coup, j'entends derriere moi un bruit de collision entre deux personnes et des cartons qui tombent.)"
    perso_joueur "(En me retournant, je vois Ema et Alix, toutes les deux par terre, en train de se disputer.)"
    perso_joueur "(Oh la la, ca peut mal finir tous ca)"
    show image_alix_enerve at right
    show image_ema_enerve at left
    perso_ema "Nan mais c'est pas possible !! Tu le fais exprès là !"
    perso_alix "Oh ça va...elle va pas commencé celle là"
    perso_ema "QUOI ?! C'est moi qui ai commencé maintenant ?! Mais tu te crois drôle en faisant ça ?!"
    perso_alix "Si je voulais être drôle je t'aurais sorti.....EEEMAcarena !AAaahhh"
    perso_ema "Et ma main dans ta gueule ?!!"
    $perso_alix ("Ohh trop bon jeu de mots, Ema main dans ta gueule ! Tu vois que t'as de l'humour !", interact = False)
    $result_43 = renpy.display_menu ([("Prendre la défense d'Alix", "un"), ("Prendre la défense d'Ema", "deux"), ("Aller voir Rebecca", "trois")])
    if result_43 == "un":
        $affinite_alix += 10
        $affinite_ema -= 10
        perso_joueur "Oh trop marrant Alix !!! J'y avais pas penser a celle-là !!"
        perso_ema "Mais t'es sérieux à trouver ça marrant ???"
        perso_ema "J'y crois pas tous le monde à décider de me les briser aujourd'hui !!"
        perso_ema "Mais t'es sérieux à trouver ça marrant ???"
        perso_ema "Alix, viens la... Je vais t'annihiler !!"
        hide image_ema_enerve
        hide image_alix_enerve
        show image_theo_normal
        perso_theo "Hé oh !! C'est quoi cet étang tout boueux la !"
        perso_theo "Les enfants on est en colo ! On est pas venu la pour se brouiller comme des œufs, alors tous le monde se sépare !"
        perso_theo "Vous reprenez le travail et le premier que je vois a embêter ses camarades peut oublier la boum de ce soir !"
        perso_joueur "Heureusement que Théo était la sinon ça aurait pu mal finir."
        perso_joueur "Au moins, tout est rentré dans l'ordre, maintenant je vais retourner dans mon dortoir... Il faut que je me prépare pour ce soir..."

    if result_43 == "deux":
        $affinite_alix -= 10
        $affinite_ema += 10
        perso_joueur "Alix, calme toi un peu... T'abuse là."
        hide image_ema_enerve
        hide image_alix_enerve
        show image_ema_sourire at left
        show image_alix_pleure at right
        perso_ema "Ah merci Bambi !"
        perso_alix "Bah pourquoi, j'ai juste fais des petites blagues..."
        perso_ema ""
        hide image_ema_enerve
        hide image_alix_enerve
        show image_theo_normal
        perso_theo "Hé oh !! C'est quoi cet étang tout boueux la !"
        perso_theo "Les enfants on est en colo ! On est pas venu la pour se brouiller comme des œufs, alors tous le monde se sépare !"
        perso_theo "Vous reprenez le travail et le premier que je vois a embêter ses camarades peut oublier la boum de ce soir !"
        perso_joueur "Heureusement que Théo était la sinon ça aurait pu mal finir."
        perso_joueur "Au moins, tout est rentré dans l'ordre, maintenant je vais retourner dans mon dortoir... Il faut que je me prépare pour ce soir..."

    if result_43 == "trois":
        $affinite_rebecca += 10
        perso_joueur "(Je vais peut etre pas m'interposer... Ca risque de tourner au vinaigre... Je vais peut etre aller voir Rebecca)"
        hide image_ema_enerve
        hide image_alix_enerve
        show image_rebecca_normal
        perso_joueur "Tu trouves pas qu'elles abusent un peu ?"
        perso_rebecca "Si...peut-être un peu....J'espère que ça ne va pas finir en bagarre...."
        perso_joueur "Toi au moins, tu t'emporte pas aussi vite"
        hide image_rebecca_normal
        show image_theo_normal
        hide image_ema_enerve
        hide image_alix_enerve
        show image_theo_normal
        perso_theo "Hé oh !! C'est quoi cet étang tout boueux la !"
        perso_theo "Les enfants on est en colo ! On est pas venu la pour se brouiller comme des œufs, alors tous le monde se sépare !"
        perso_theo "Vous reprenez le travail et le premier que je vois a embêter ses camarades peut oublier la boum de ce soir !"
        perso_joueur "Heureusement que Théo était la sinon ça aurait pu mal finir."
        perso_joueur "Au moins, tout est rentré dans l'ordre, maintenant je vais retourner dans mon dortoir... Il faut que je me prépare pour ce soir..."

    hide screen halter_6

    scene fond_couloir_nuit
    show fond_couloir_nuit

    if (affinite_alix > 80 and affinite_ema > 80 and affinite_rebecca > 80 and nombre_recup >= 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_44 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Rebecca", "deux"), ("Aller demander à Ema", "trois"), ("Aller demander à Théo", "quatre")])
        if result_44 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire

            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            label suite_rythm_alix:
            window show
            $ quick_menu = True
            hide screen show_game
            pause(1)
            scene fin_alix with fade

            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_44 == "deux":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rebecca.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            label suite_rythm_rebecca:
            window show
            $ quick_menu = True
            hide screen show_game
            pause(1)
            scene fin_rebecca with fade
            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_44 == "trois":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            label suite_rythm_ema:
            window show
            $ quick_menu = True
            hide screen show_game
            pause(1)
            scene fin_ema with fade
            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_44 == "quatre":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return



    if (affinite_alix > 80 and affinite_ema > 80 and affinite_rebecca > 80 and nombre_recup < 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_44 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Rebecca", "deux"), ("Aller demander à Ema", "trois")])
        if result_44 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            window show
            $ quick_menu = True
            hide screen show_game
            pause(1)
            scene fin_alix

            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_44 == "deux":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rebecca.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            window show
            $ quick_menu = True
            hide screen show_game
            pause(1)
            scene fin_rebecca

            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_44 == "trois":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause(1)
            scene fin_ema with fade
            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return


    if (affinite_alix > 80 and affinite_ema > 80 and affinite_rebecca < 80 and nombre_recup >= 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_45 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Ema", "deux"), ("Aller demander à Théo", "trois")])
        if result_45 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_alix with fade
            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_45 == "deux":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = False
            pause (1)
            scene fin_ema with fade

            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_45 == "trois":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix > 80 and affinite_ema > 80 and affinite_rebecca < 80 and nombre_recup < 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_45 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Ema", "deux")])
        if result_45 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            window show
            $ quick_menu = True
            hide screen show_game
            pause (1)
            scene fin_alix with fade

            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_45 == "deux":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_ema with fade

            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix > 80 and affinite_ema < 80 and affinite_rebecca > 80 and nombre_recup >= 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_46 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Rebecca", "deux"), ("Aller demander à Théo", "trois")])
        if result_46 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            scene fin_alix with fade
            pause (1)
            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_46 == "deux":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rythm.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rebecca.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_rebecca with fade
            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_46 == "trois":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix > 80 and affinite_ema < 80 and affinite_rebecca > 80 and nombre_recup < 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_46 = renpy.display_menu([("Aller demander à Alix", "un"), ("Aller demander à Rebecca", "deux")])
        if result_46 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_alix with fade
            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_46 == "deux":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rythm.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rebecca.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause(1)
            scene fin_rebecca

            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix < 80 and affinite_ema > 80 and affinite_rebecca > 80 and nombre_recup >= 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_47 = renpy.display_menu([("Aller demander à Ema", "deux"), ("Aller demander à Rebecca", "un"), ("Aller demander à Théo", "trois")])
        if result_47 == "un":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            perso_joueur "(Oh, elle me tient la main...)"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rebecca.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_rebecca
            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"
            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_47 == "deux":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_ema with fade
            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_47 == "trois":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix < 80 and affinite_ema > 80 and affinite_rebecca > 80 and nombre_recup < 10):
        $ perso_joueur ("(Bon maintenant que je me suis préparer, je vais devoir choisir la personne qui va m'accompagner.)", interact = False)
        $ result_47 = renpy.display_menu([("Aller demander à Ema", "deux"), ("Aller demander à Rebecca", "un")])
        if result_47 == "un":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rebecca.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_rebecca with fade
            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"
            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_47 == "deux":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_ema with fade
            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return


    if (affinite_alix > 80 and affinite_ema < 80 and affinite_rebecca < 80 and nombre_recup >= 10):
        $ perso_joueur ("Bon, maintenant que je me suis préparé, je dois choisir qui va m'accompagner", interact = False)
        $ result_50 = renpy.display_menu([("Aller demander à Alix","un"), ("Aller demander à Théo","deux")])
        if result_50 == "un":
            show image_alix_sourire
            perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
            perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_alix_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_alix_sourire
            show screen timeup_alix()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_alix.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_alix with fade
            perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
            perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
            perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
            perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"
            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_50 == "deux":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix > 80 and affinite_ema < 80 and affinite_rebecca < 80 and nombre_recup < 10):
        show image_alix_sourire
        perso_joueur "Salut Alix, ça te dirait d'aller à la boom avec moi ?"
        perso_alix "Ouais je veux bien ! En plus, j'adore danser !"
        perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
        perso_joueur "Allez, on y va !"
        scene fond_boom_fete
        show image_alix_sourire
        perso_joueur "(Oh, elle me tient la main...)"
        perso_joueur "Dansons !"
        hide image_alix_sourire
        show screen timeup_alix()
        window hide
        $ quick_menu = False
        stop music
        play music "../audio/musique_alix.mp3"
        show fond_rythm
        show nenuphar_1
        show nenuphar_2
        show nenuphar_3
        python:
            hits = 0
            misses = 0
            t = time.time()
            manager = SpriteManager(update = sprites_update, event = sprites_event)
            sprite = Image("../images/rose.png")
            sprites = []
            td = 0
            td_2 = 0
            td_3 = 0
            for i in xrange(20):
                td += renpy.random.random() + 1.5
                td_2 += renpy.random.random() + 1.5
                td_3 += renpy.random.random() + 1.5
                sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td, -50, 150))
                sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_2, -50, 310))
                sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 40, td_3, -50, 460))
            renpy.show_screen("show_game")
            renpy.show("_", what=manager, zorder = 1)

        while True:
            $ result = ui.interact()
        hide screen show_game
        window show
        $ quick_menu = True
        pause (1)
        scene fin_alix with fade
        perso_joueur "Tu sais Alix... Je t'apprécie beaucoup."
        perso_alix "Oh oui, moi aussi je t'aime beaucoup Anthony. J'ai fait que de penser à toi durant les 3 jours où tu étais la. J'attendais juste de te voir tous les jours..."
        perso_joueur "Ca te dit, on s'echange nos numéros et on se revoit aprés la colo?"
        perso_alix "Oh ouiiiii, comme ca je t'enverrai plein de messages avec plein de coeur! Et on pourra aller faire de l'escalade ensembles!"
        perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Alix, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause ((30))
        return

    if (affinite_alix < 80 and affinite_ema > 80 and affinite_rebecca < 80 and nombre_recup >= 10):
        $ perso_joueur ("Bon, maintenant que je me suis préparé, je dois demander à quelqu'un de m'accompagner", interact = False)
        $ result_51 = renpy.display_menu([("Aller demander à Ema","un"), ("Aller demander à Théo","deux")])
        if result_51 == "un":
            show image_ema_sourire
            perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
            perso_ema "Ah... Moi ? Ouais, je veux bien !"
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_ema_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_ema_sourire
            show screen timeup_ema()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_ema.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_ema with fade
            perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
            perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
            perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
            perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"


            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

        if result_51 == "deux":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix < 80 and affinite_ema > 80 and affinite_rebecca < 80 and nombre_recup < 10):
        show image_ema_sourire
        perso_joueur "Salut Ema, ça te dirait d'aller à la boom avec moi ?"
        perso_ema "Ah... Moi ? Ouais, je veux bien !"
        perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
        perso_joueur "Allez, on y va !"
        scene fond_boom_fete
        show image_ema_sourire
        perso_joueur "(Oh, elle me tient la main...)"
        perso_joueur "Dansons !"
        hide image_ema_sourire
        show screen timeup_ema()
        window hide
        $ quick_menu = False
        stop music
        play music "../audio/musique_ema.mp3"
        show fond_rythm
        show nenuphar_1
        show nenuphar_2
        show nenuphar_3
        python:
            hits = 0
            misses = 0
            t = time.time()
            manager = SpriteManager(update = sprites_update, event = sprites_event)
            sprite = Image("../images/rose.png")
            sprites = []
            td = 0
            td_2 = 0
            td_3 = 0
            for i in xrange(20):
                td += renpy.random.random() + 1.5
                td_2 += renpy.random.random() + 1.5
                td_3 += renpy.random.random() + 1.5
                sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td, -50, 150))
                sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_2, -50, 310))
                sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 30, td_3, -50, 460))
            renpy.show_screen("show_game")
            renpy.show("_", what=manager, zorder = 1)

        while True:
            $ result = ui.interact()
        hide screen show_game
        window show
        $ quick_menu = True
        pause (1)
        scene fin_ema with fade
        perso_joueur "Tu sais Ema... Je t'apprécie beaucoup."
        perso_ema "Bambi, je t'aime bien moi aussi. Ca faisait lomgtemps que je t'avais pas vu et te revoir dans cette colo m'a ouvert les yeux : T'es vraiment un mec en or"
        perso_joueur "Haha merci Ema... Faut qu'on se revoit en dehors. Mes parents seraient contents de te revoir."
        perso_ema "Bon c'est pas le tout... mais on m'attend pour le karaoké. Je vais leur montrer qui est la meilleure. Je te dédie cette chanson Anthony"
        perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Ema, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause ((30))
        return


    if (affinite_alix < 80 and affinite_ema < 80 and affinite_rebecca > 80 and nombre_recup >= 10):
        $ perso_joueur ("Bon, maintenant que je me suis préparé, je dois demander à quelqu'un de m'accompagner", interact = False)
        $ result_52 = renpy.display_menu([("Aller demander à Rebecca","un"), ("Aller demander à Théo","deux")])
        if result_52 == "un":
            show image_rebecca_sourire
            perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
            perso_rebecca "Ah... Euh... Oui, je veux bien."
            perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
            perso_joueur "Allez, on y va !"
            scene fond_boom_fete
            show image_rebecca_sourire
            perso_joueur "(Oh, elle me tient la main...)"
            perso_joueur "Dansons !"
            hide image_rebecca_sourire
            show screen timeup_rebecca()
            window hide
            $ quick_menu = False
            stop music
            play music "../audio/musique_rebecca.mp3"
            show fond_rythm
            show nenuphar_1
            show nenuphar_2
            show nenuphar_3
            python:
                hits = 0
                misses = 0
                t = time.time()
                manager = SpriteManager(update = sprites_update, event = sprites_event)
                sprite = Image("../images/rose.png")
                sprites = []
                td = 0
                td_2 = 0
                td_3 = 0
                for i in xrange(20):
                    td += renpy.random.random() + 1.5
                    td_2 += renpy.random.random() + 1.5
                    td_3 += renpy.random.random() + 1.5
                    sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                    sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                    sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
                renpy.show_screen("show_game")
                renpy.show("_", what=manager, zorder = 1)

            while True:
                $ result = ui.interact()
            hide screen show_game
            window show
            $ quick_menu = True
            pause (1)
            scene fin_rebecca with fade
            perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
            perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
            perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
            perso_rebecca "Oui... plus qu'un ami"
            perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"


            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return
        if result_52 == "deux":
            scene fond_boom_fete
            show image_theo_normal
            perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
            hide image_theo_normal
            show image_theo_blush
            perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
            perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
            perso_theo "Et c'est pour cela..."
            hide image_theo_blush
            scene fin_theo with fade
            perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
            perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"

            scene credits with fade
            window hide
            $ quick_menu = False
            pause ((30))
            return

    if (affinite_alix < 80 and affinite_ema < 80 and affinite_rebecca > 80 and nombre_recup < 10):
        show image_rebecca_sourire
        perso_joueur "Salut Rebecca, ça te dirait d'aller à la boom avec moi ?"
        perso_rebecca "Ah... Euh... Oui, je veux bien."
        perso_joueur "Je suis trop content que tu acceptes de venir avec moi..."
        perso_joueur "Allez, on y va !"
        scene fond_boom_fete
        show image_rebecca_sourire
        perso_joueur "(Oh, elle me tient la main...)"
        perso_joueur "Dansons !"
        hide image_rebecca_sourire
        show screen timeup_rebecca()
        window hide
        $ quick_menu = False
        stop music
        play music "../audio/musique_rebecca.mp3"
        show fond_rythm
        show nenuphar_1
        show nenuphar_2
        show nenuphar_3
        python:
            hits = 0
            misses = 0
            t = time.time()
            manager = SpriteManager(update = sprites_update, event = sprites_event)
            sprite = Image("../images/rose.png")
            sprites = []
            td = 0
            td_2 = 0
            td_3 = 0
            for i in xrange(20):
                td += renpy.random.random() + 1.5
                td_2 += renpy.random.random() + 1.5
                td_3 += renpy.random.random() + 1.5
                sprites_1 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td, -50, 150))
                sprites_2 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_2, -50, 310))
                sprites_3 = sprites.append(Rhythm(Image("../images/rose.png"), 20, td_3, -50, 460))
            renpy.show_screen("show_game")
            renpy.show("_", what=manager, zorder = 1)
        while True:
            $ result = ui.interact()
        window show
        $ quick_menu = False
        hide screen show_game
        pause (1)
        scene fin_rebecca with fade
        perso_joueur "Tu sais Rebecca... Je t'apprécie beaucoup."
        perso_rebecca "Moi aussi, je t'aime beaucoup... Depuis que je t'ai rencontrée, j'ai eu l'impression de m'ouvrir de plus en plus au monde. Je me sens comme différente... Je te dois tellement"
        perso_joueur "Moi, j'ai rencontré une sacré personne. Au premier contact, tu étais timide et distante et maintenant tu t'adresse à moi comme un ami... ou plus qu'un ami"
        perso_rebecca "Oui... plus qu'un ami"
        perso_joueur "(Je suis arrivé dans cette colonie de vacances en pensant que je m'ennuierai. Mais finalement, c'etait marrant.. Avec le moniteur, les filles et surtout Rebecca, j'ai passé les meilleures vacances... Je reviendrai surement l'année prochaine.)"

        scene credits with fade
        window hide
        $ quick_menu = False
        pause ((30))
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_rebecca < 80 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_rebecca < 80 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_ema < 80 and affinite_ema > 20 and affinite_alix < 80 and affinite_rebecca < 80 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_ema < 80 and affinite_ema > 20 and affinite_alix < 80 and affinite_rebecca < 80 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_rebecca < 80 and affinite_rebecca > 20 and affinite_ema < 80 and affinite_alix < 80 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_rebecca < 80 and affinite_rebecca > 20 and affinite_ema < 80 and affinite_alix < 80 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_rebecca < 80 and affinite_rebecca > 20 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_rebecca < 80 and affinite_rebecca > 20 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and affinite_rebecca > 20 and affinite_alix < 80 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_alix < 80 and affinite_alix > 20 and affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and affinite_rebecca > 20 and nombre_recup >= 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene fond_boom_fete
        show image_theo_normal
        perso_joueur "Monsieur, j'ai trouvé des haltères durant le séjour! J'ai pensé que ca pourrait vous interesser..."
        hide image_theo_normal
        show image_theo_blush
        perso_theo "OOooohhh ! Merci Anthony, c'est trop mignon."
        perso_theo "Tu as tout de suite pensé à moi quand tu as trouvé ses haltères. C'est une belle preuve d'amour pour ton moniteur favori..."
        perso_theo "Et c'est pour cela..."
        hide image_theo_blush
        scene fin_theo with fade
        perso_theo "QUE TU VAS RESTER AVEC MOI DANS LA COLO TOUT L'ÉTÉ POUR M'AIDER... VIENS LA QUE JE T'EMBRASSE"
        perso_joueur "AAAaaaaaah, je sais que vous m'aimez bien, mais quand même!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    if (affinite_ema < 80 and affinite_ema > 20 and affinite_rebecca < 80 and affinite_rebecca > 20 and affinite_alix < 80 and affinite_alix > 20 and nombre_recup < 10):
        perso_joueur "(Bon... J'ai personne avec qui danser avec moi... Comment j'ai fait pour me retrouver seul comme ça ?)"
        perso_joueur "(Peut-être que je n'ai pas été assez sympa avec les filles ces trois derniers jours ?)"
        show image_theo_sourire
        perso_theo "Bah alors, tu n'oses pas demander à une rainette de danser avec toi ?"
        perso_theo "C'est pas grave tu n'as qu'à venir avec moi et mes deux copains..."
        hide image_theo_sourire
        show image_theo_muscle
        perso_theo "BANG !!"
        hide image_theo_muscle
        show image_theo_muscle_inverse
        perso_theo "BOUM !!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return

    #choix Alix


    #choix Rebecca


    #choix Ema


    #choix Theo

    if (affinite_alix < 20 and affinite_ema < 20 and affinite_rebecca < 20):
        scene fond_foret_nuit
        show image_rebecca_normal at right
        show image_ema_normal
        show image_alix_normal at left
        perso_alix "Hey ! On voulait te parler avec les deux autres filles, mais on s'entend pas avec cette musique, viens on va un peu plus loin, au calme."
        perso_joueur "(Je commence à suivre les trois filles, je me demande bien ce qu'elles veulent me dire.)"
        scene bad_end with fade
        stop music
        play music "../audio/musique_bad_end.mp3" fadein 0.1
        perso_meta "CRÈVE !!!"
        scene credits with fade
        window hide
        $ quick_menu = False
        pause (30)
        return
return
