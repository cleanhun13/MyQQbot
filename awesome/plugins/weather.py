from nonebot import on_command, CommandSession


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    #得到消息的内容，并去掉首尾的空白符
    city = session.current_arg_text.strip()
    # 如果除了命令的名字之外用户还提供了别的内容，即用户直接将城市名跟在命令名后面，
    # 则此时 city 不为空。例如用户可能发送了："天气 南京"，则此时 city == '南京'
    # 否则这代表用户仅发送了："天气" 二字，机器人将会向其发送一条消息并且等待其回复

    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()

        # 如果继续为空白字符则继续询问
        while not city:
            city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
        # 获取城市的天气预报
        weather_report = await get_weather_of_city(city)
        # 发送天气预报
        await session.send(weather_report)


async def get_weather_of_city(city: str) -> str:
    # 简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    return f'{city}的天气是...'