---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - databases
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format at which the backup was created. |
| <CopyableCode code="size_gigabytes" /> | `number` | The size of the database backup in GBs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_backups" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> |
| <CopyableCode code="_list_backups" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> |
