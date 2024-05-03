---
title: sts_delegates
hide_title: false
hide_table_of_contents: false
keywords:
  - sts_delegates
  - gcp_integration
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sts_delegates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.gcp_integration.sts_delegates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the delegate service account. |
| <CopyableCode code="attributes" /> | `object` | Your delegate account attributes. |
| <CopyableCode code="type" /> | `string` | The type of account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_gcpsts_delegate" /> | `SELECT` | <CopyableCode code="dd_site" /> | List your Datadog-GCP STS delegate account configured in your Datadog account. |
| <CopyableCode code="_get_gcpsts_delegate" /> | `EXEC` | <CopyableCode code="dd_site" /> | List your Datadog-GCP STS delegate account configured in your Datadog account. |
| <CopyableCode code="make_gcpsts_delegate" /> | `EXEC` | <CopyableCode code="dd_site" /> | Create a Datadog GCP principal. |
