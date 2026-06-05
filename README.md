# PythaiNAV: ทำให้การดึงข้อมูลกองทุนไทยเป็นเรื่องง่าย
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FCircleOnCircles%2Fpythainav.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FCircleOnCircles%2Fpythainav?ref=badge_shield)
![Tests](https://github.com/ninyawee/pythainav/workflows/Tests/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/ninyawee/pythainav/branch/develop/graph/badge.svg)](https://codecov.io/gh/ninyawee/pythainav)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f868488db4ba4266a112c3432301c6b4)](https://www.codacy.com/manual/nutchanon/pythainav?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ninyawee/pythainav&amp;utm_campaign=Badge_Grade)



![cover image](https://github.com/ninyawee/pythainav/raw/master/extra/pythainav.png)



> อยากชวนทุกคนมาร่วมพัฒนา ติชม แนะนำ เพื่อให้ทุกคนเข้าถึงข้อมูลการง่ายขึ้น [เริ่มต้นได้ที่นี้](https://github.com/ninyawee/pythainav/issues) หรือเข้ามา Chat ใน [Discord](https://discord.gg/jjuMcKZ) ได้เลย 😊

📖 Documentation is here. คู่มือการใช้งานอยู่ที่นี่ <https://pythainav.nutchanon.org/>

## Get Started - เริ่มต้นใช้งาน

```bash
$ pip install pythainav
```

```python
import pythainav as nav

nav.get("KT-PRECIOUS")
> Nav(value=4.2696, updated='20/01/2020', tags={'latest'}, fund='KT-PRECIOUS')

nav.get("TISTECH-A", date="1 week ago")
> Nav(value=12.9976, updated='14/01/2020', tags={}, fund='TISTECH-A')

nav.get_all("TISTECH-A", range="MAX")
> [Nav(value=12.9976, updated='21/01/2020', tags={}, fund='TISTECH-A'), Nav(value=12.9002, updated='20/01/2020', tags={}, fund='TISTECH-A'), ...]

nav.get_all("KT-PRECIOUS", asDataFrame=True)
> pd.DataFrame [2121 rows x 4 columns]
```

## Source of Data - ที่มาข้อมูล

ดูจาก <https://pythainav.nutchanon.org/datasource/>

## Disclaimer

เราไม่รับประกันความเสียหายใดๆทั้งสิ้นที่เกิดจาก แหล่งข้อมูล, library, source code,sample code, documentation, library dependencies และอื่นๆ

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://nutchanon.org"><img src="https://avatars2.githubusercontent.com/u/8089231?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nutchanon Ninyawee</b></sub></a><br /><a href="https://github.com/ninyawee/pythainav/commits?author=ninyawee" title="Code">💻</a> <a href="#infra-ninyawee" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/sctnightcore"><img src="https://avatars2.githubusercontent.com/u/23263315?v=4?s=100" width="100px;" alt=""/><br /><sub><b>sctnightcore</b></sub></a><br /><a href="https://github.com/ninyawee/pythainav/commits?author=sctnightcore" title="Code">💻</a> <a href="#talk-sctnightcore" title="Talks">📢</a> <a href="#ideas-sctnightcore" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/angonyfox"><img src="https://avatars3.githubusercontent.com/u/1295513?v=4?s=100" width="100px;" alt=""/><br /><sub><b>angonyfox</b></sub></a><br /><a href="https://github.com/ninyawee/pythainav/commits?author=angonyfox" title="Code">💻</a> <a href="https://github.com/ninyawee/pythainav/commits?author=angonyfox" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/samupra"><img src="https://avatars.githubusercontent.com/u/24209940?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pongpira Upra</b></sub></a><br /><a href="https://github.com/ninyawee/pythainav/commits?author=samupra" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/namv2012"><img src="https://avatars.githubusercontent.com/u/50385570?v=4?s=100" width="100px;" alt=""/><br /><sub><b>namv2012</b></sub></a><br /><a href="https://github.com/ninyawee/pythainav/commits?author=namv2012" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FCircleOnCircles%2Fpythainav.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FCircleOnCircles%2Fpythainav?ref=badge_large)
