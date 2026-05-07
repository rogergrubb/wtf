"""WTF 9-avatar narration documentary.
Each of Runway's 9 preset avatars delivers one paragraph.
Cuts to next avatar at paragraph break.
Narration text overlaid on each segment.
"""
import json, time, os, subprocess, urllib.request, shutil
from pathlib import Path
from runwayml import RunwayML

OUT = Path('/sessions/dreamy-sleepy-archimedes/mnt/outputs')
WORK = Path('/tmp/wtf_9avatar')
WORK.mkdir(parents=True, exist_ok=True)

# 9 paragraphs, 9 avatars, 9 voices — each tuned to feel right for the line
SEGMENTS = [
    ('game-character', 'marcus',
     "On Tuesday May fifth, Number One Son Software Development asked one question. If you had to enter a hackathon hosted by the company that built every tool you would use, how would you represent yourself?"),
    ('music-superstar', 'aurora',
     "Cherry-picking three or four facets felt like dishonesty. So we built an army. Fifty-one soldiers. Each a master of one Runway capability."),
    ('game-character-man', 'vincent',
     "Number One Son is a one-founder company on a one-billion-dollar trajectory. The next great companies don't have hundreds of employees. They have one Mastermind and an army of agents."),
    ('cat-character', 'felix',
     "Ten Sergeants command. One General orchestrates. The Mastermind directs. And every shot you are about to see was produced by the army you are about to meet."),
    ('influencer', 'mia',
     "The order moves. The General receives. Sergeants stand at attention. Soldiers march in. This is what Number One Son does at scale."),
    ('tennis-coach', 'drew',
     "Forty-eight seconds of orchestration. Fifteen soldiers contributed. The Mastermind never touched a tool. The army did the work."),
    ('human-resource', 'clara',
     "Every avatar you see is a Runway preset. Every voice you hear is a Runway voice. Every shot is a Runway endpoint working in real time, in front of you."),
    ('fashion-designer', 'violet',
     "Aleph color-graded the cuts. Gen-4.5 painted the worlds. Characters spoke the lines. Sound effects scored the moments. The army works in concert."),
    ('cooking-teacher', 'georgia',
     "Number One Son did the homework. The Mastermind earned the grade. Runway Builders Program — let us talk."),
]

c = RunwayML()

# Phase A: submit all 9 avatar_videos in parallel
print("[A] Submitting 9 avatar_videos in parallel...")
tasks = []
for i, (avatar, voice, text) in enumerate(SEGMENTS, start=1):
    try:
        r = c.avatar_videos.create(
            model='gwm1_avatars',
            avatar={'preset_id': avatar, 'type': 'runway-preset'},
            speech={
                'type': 'text',
                'text': text,
                'voice': {'preset_id': voice, 'type': 'preset'},
            },
        )
        print(f"  [{i:02d}] {avatar:22s} + {voice:10s} → task {r.id[:12]}...")
        tasks.append({'idx': i, 'avatar': avatar, 'voice': voice, 'text': text,
                      'task_id': r.id, 'submitted_at': time.time()})
    except Exception as e:
        print(f"  [{i:02d}] {avatar} FAILED: {type(e).__name__}: {str(e)[:200]}")
        tasks.append({'idx': i, 'avatar': avatar, 'voice': voice, 'text': text,
                      'task_id': None, 'error': str(e)[:200]})

with open(WORK / 'tasks.json', 'w') as f:
    json.dump(tasks, f, indent=2)
print(f"  submitted {sum(1 for t in tasks if t['task_id'])} of {len(tasks)} tasks")

o = c.organization.retrieve()
print(f"  credits remaining: {o.credit_balance}")
