def draw_text(screen, font, font_color, text, pos):
    if isinstance(text, str):
        text_img = font.render(text, True, font_color)
        text_rect = text_img.get_rect(center=pos)
        screen.blit(text_img, text_rect)
    elif isinstance(text, list):
        for line in text:
            text_img = font.render(line, True, font_color)
            text_rect = text_img.get_rect(center=pos)
            screen.blit(text_img, text_rect)
            pos = (pos[0], pos[1] + 30)
