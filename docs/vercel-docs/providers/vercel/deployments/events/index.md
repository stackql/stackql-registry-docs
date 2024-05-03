---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - deployments
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.deployments.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="__created" /> | `number` |
| <CopyableCode code="__payload" /> | `object` |
| <CopyableCode code="__type" /> | `string` |
| <CopyableCode code="_created" /> | `number` |
| <CopyableCode code="_payload" /> | `object` |
| <CopyableCode code="_type" /> | `string` |
| <CopyableCode code="created" /> | `number` |
| <CopyableCode code="payload" /> | `object` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_deployment_events" /> | `SELECT` | <CopyableCode code="idOrUrl, teamId" /> |
