def draw_text(screen, font, font_color, text, pos):
    text = font.render(text, True, font_color)
    text_rect = text.get_rect(center=pos)
    screen.blit(text, text_rect)
