---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apps
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="appDefinition" /> | `object` |
| <CopyableCode code="appManifest" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getApp" /> | `SELECT` | <CopyableCode code="uuid, region" /> | Gets the app with the given universally unique identifier (UUID). |
| <CopyableCode code="listApps" /> | `SELECT` | <CopyableCode code="region" /> | Lists all available apps from the App Catalog. |
