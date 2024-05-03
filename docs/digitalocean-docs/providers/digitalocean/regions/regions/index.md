---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - regions
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.regions.regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The display name of the region.  This will be a full name that is used in the control panel and other interfaces. |
| <CopyableCode code="available" /> | `boolean` | This is a boolean value that represents whether new Droplets can be created in this region. |
| <CopyableCode code="features" /> | `` | This attribute is set to an array which contains features available in this region |
| <CopyableCode code="sizes" /> | `` | This attribute is set to an array which contains the identifying slugs for the sizes available in this region. |
| <CopyableCode code="slug" /> | `string` | A human-readable string that is used as a unique identifier for each region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
