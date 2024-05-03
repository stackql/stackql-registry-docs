---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="continent" /> | `string` |  |
| <CopyableCode code="data_centers" /> | `array` |  |
| <CopyableCode code="default" /> | `boolean` | Whether or not the region is presented as the default. |
| <CopyableCode code="disabled" /> | `boolean` |  |
| <CopyableCode code="flag" /> | `string` |  |
| <CopyableCode code="label" /> | `string` |  |
| <CopyableCode code="reason" /> | `string` |  |
| <CopyableCode code="slug" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_regions" /> | `SELECT` |  |
| <CopyableCode code="_list_regions" /> | `EXEC` |  |
