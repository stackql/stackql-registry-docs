---
title: transfer_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_logs
  - bigquerydatatransfer
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigquerydatatransfer.transfer_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="messageText" /> | `string` | Message text. |
| <CopyableCode code="messageTime" /> | `string` | Time when message was logged. |
| <CopyableCode code="severity" /> | `string` | Message severity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_transfer_configs_runs_transfer_logs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, runsId, transferConfigsId" /> |
| <CopyableCode code="projects_transfer_configs_runs_transfer_logs_list" /> | `SELECT` | <CopyableCode code="projectsId, runsId, transferConfigsId" /> |
| <CopyableCode code="_projects_locations_transfer_configs_runs_transfer_logs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, runsId, transferConfigsId" /> |
| <CopyableCode code="_projects_transfer_configs_runs_transfer_logs_list" /> | `EXEC` | <CopyableCode code="projectsId, runsId, transferConfigsId" /> |
