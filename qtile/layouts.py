from libqtile import layout
from libqtile.config import Match

column_layout = layout.Columns(
        border_focus="#3489eb",
        # border_focus="#ffffff",
        border_on_single=True,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=0,
        margin=5
    )

layouts = [
    column_layout,
    layout.Max(
        border_focus="#3489eb",
        border_width=0,
        margin=5
    ),
]

floating_layout = layout.Floating(
    border_focus="#000000",
    border_normal="#000000",
    border_width=0,
    float_rules=[
        Match(title="rmenu")
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        # Match(wm_class="confirmreset"),  # gitk
        # Match(wm_class="makebranch"),  # gitk
        # Match(wm_class="maketag"),  # gitk
        # Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(title="branchdialog"),  # gitk
        # Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="zoom.real "),
    ]
)
