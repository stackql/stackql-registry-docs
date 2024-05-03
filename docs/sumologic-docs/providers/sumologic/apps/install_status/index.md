---
title: install_status
hide_title: false
hide_table_of_contents: false
keywords:
  - install_status
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
<tr><td><b>Name</b></td><td><code>install_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.apps.install_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | Whether or not the request is in progress (`InProgress`), has completed successfully (`Success`), or has completed with an error (`Failed`). |
| <CopyableCode code="statusMessage" /> | `string` | Additional status message generated if the status is not `Failed`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getAsyncInstallStatus" /> | `SELECT` | <CopyableCode code="jobId, region" /> |
