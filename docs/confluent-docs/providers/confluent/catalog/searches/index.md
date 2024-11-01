---
title: searches
hide_title: false
hide_table_of_contents: false
keywords:
  - searches
  - catalog
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.searches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="entities" /> | `array` | The entities |
| <CopyableCode code="referredEntities" /> | `object` | The referred entities |
| <CopyableCode code="searchParameters" /> | `object` | Search paramas to filter results |
| <CopyableCode code="types" /> | `array` | The types |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="search_using_attribute" /> | `SELECT` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve data for the specified attribute search query. |
| <CopyableCode code="search_using_basic" /> | `SELECT` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve data for the specified fulltext query. |
