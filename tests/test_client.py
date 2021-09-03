import pytest


@pytest.mark.asyncio
async def test_get_teams_no_team(test_client):
    test_client["httpx_mock"].add_response(method="GET", json=[])
    teams = list()
    async for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 0


@pytest.mark.asyncio
async def test_get_teams_one_team(test_client, fake_team):
    test_client["httpx_mock"].add_response(method="GET", json=fake_team.dict())
    teams = list()
    async for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 1
    assert teams[0].name == fake_team.name


@pytest.mark.asyncio
async def test_get_teams_many_teams(test_client, fake_team):
    test_client["httpx_mock"].add_response(
        method="GET", json=[fake_team.dict(), fake_team.dict()]
    )
    teams = list()
    async for team in test_client["client"].teams.list():
        teams.append(team)

    assert len(teams) == 2
    assert teams[0].name == fake_team.name
    assert teams[1].name == fake_team.name
