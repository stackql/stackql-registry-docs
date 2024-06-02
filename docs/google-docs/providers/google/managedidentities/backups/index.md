---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - managedidentities
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="managedidentities.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique name of the Backup in the form of `projects/&#123;project_id&#125;/locations/global/domains/&#123;domain_name&#125;/backups/&#123;name&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the backups was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the current status of this backup, if available. |
| <CopyableCode code="type" /> | `string` | Output only. Indicates whether it’s an on-demand backup or scheduled. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Gets details of a single Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainsId, projectsId" /> | Lists Backup in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="domainsId, projectsId" /> | Creates a Backup for a domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Deletes identified Backup. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="domainsId, projectsId" /> | Lists Backup in a given project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Updates the labels for specified Backup. |
