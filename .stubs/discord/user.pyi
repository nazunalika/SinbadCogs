import discord.abc

from .channel import DMChannel, GroupChannel
from .enums import (
    DefaultAvatar,
    HypeSquadHouse,
    PremiumType,
    UserContentFilter,
    FriendFlags,
    Status,
    Theme,
)
from .colour import Colour
from .guild import Guild
from .http import _ClientUserDict
from .permissions import Permissions
from .message import Message
from .relationship import Relationship
from .asset import Asset

import datetime
from typing import Any, Optional, NamedTuple, List, Set, Dict
from typing_extensions import Literal

_VALID_STATIC_FORMATS = Literal["jpeg", "jpg", "webp", "png"]
_VALID_AVATAR_FORMATS = Literal[_VALID_STATIC_FORMATS, "gif"]

class Profile(NamedTuple):
    flags: int
    user: User
    mutual_guilds: List[Guild]
    connected_accounts: List[Any]
    premium_since: Optional[datetime.datetime]
    premium: bool
    @property
    def nitro(self) -> bool: ...
    @property
    def staff(self) -> bool: ...
    @property
    def partner(self) -> bool: ...
    @property
    def bug_hunter(self) -> bool: ...
    @property
    def early_supporter(self) -> bool: ...
    @property
    def hypesquad(self) -> bool: ...
    @property
    def hypesquad_houses(self) -> List[HypeSquadHouse]: ...

_BaseUser = discord.abc.User

class BaseUser(_BaseUser):
    name: str
    id: int
    discriminator: str
    avatar: Optional[str]
    bot: bool
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def avatar_url(self) -> Asset: ...
    def is_avatar_animated(self) -> bool: ...
    def avatar_url_as(
        self,
        *,
        format: Optional[_VALID_AVATAR_FORMATS] = ...,
        static_format: _VALID_STATIC_FORMATS = ...,
        size: int = ...,
    ) -> Asset: ...
    @property
    def default_avatar(self) -> DefaultAvatar: ...
    @property
    def default_avatar_url(self) -> Asset: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    @property
    def mention(self) -> str: ...
    def permissions_in(self, channel: discord.abc.GuildChannel) -> Permissions: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def display_name(self) -> str: ...
    def mentioned_in(self, message: Message) -> bool: ...

class ClientUser(BaseUser):
    verified: bool
    email: Optional[str]
    locale: Optional[str]
    mfa_enabled: bool
    premium: bool
    premium_type: Optional[PremiumType]
    def get_relationship(self, user_id: int) -> Optional[Relationship]: ...
    @property
    def relationships(self) -> List[Relationship]: ...
    @property
    def friends(self) -> List[User]: ...
    @property
    def blocked(self) -> List[User]: ...
    async def edit(
        self,
        *,
        password: str = ...,
        new_password: str = ...,
        email: str = ...,
        username: str = ...,
        avatar: bytes = ...,
    ) -> None: ...
    async def create_group(self, *recipients: User) -> GroupChannel: ...
    async def edit_settings(
        self,
        *,
        afk_timeout: int = ...,
        animate_emojis: bool = ...,
        convert_emoticons: bool = ...,
        default_guilds_restricted: bool = ...,
        detect_platform_accounts: bool = ...,
        developer_mode: bool = ...,
        disable_games_tab: bool = ...,
        enable_tts_command: bool = ...,
        explicit_content_filter: UserContentFilter = ...,
        friend_source_flags: FriendFlags = ...,
        gif_auto_play: bool = ...,
        guild_positions: List[discord.abc.Snowflake] = ...,
        inline_attachment_media: bool = ...,
        inline_embed_media: bool = ...,
        locale: str = ...,
        message_display_compact: bool = ...,
        render_embeds: bool = ...,
        render_reactions: bool = ...,
        restricted_guilds: List[discord.abc.Snowflake] = ...,
        show_current_game: bool = ...,
        status: Status = ...,
        theme: Theme = ...,
        timezone_offset: int = ...,
    ) -> _ClientUserDict: ...

class User(BaseUser, discord.abc.Messageable):
    @property
    def dm_channel(self) -> Optional[DMChannel]: ...
    async def create_dm(self) -> DMChannel: ...
    @property
    def relationship(self) -> Optional[Relationship]: ...
    async def mutual_friends(self) -> List[User]: ...
    def is_friend(self) -> bool: ...
    def is_blocked(self) -> bool: ...
    async def block(self) -> None: ...
    async def unblock(self) -> None: ...
    async def remove_friend(self) -> None: ...
    async def send_friend_request(self) -> None: ...
    async def profile(self) -> Profile: ...
