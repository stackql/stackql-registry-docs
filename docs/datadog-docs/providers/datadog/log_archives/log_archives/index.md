---
title: log_archives
hide_title: false
hide_table_of_contents: false
keywords:
  - log_archives
  - log_archives
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
<tr><td><b>Name</b></td><td><code>log_archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.log_archives.log_archives" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The archive ID. |
| <CopyableCode code="attributes" /> | `object` | The attributes associated with the archive. |
| <CopyableCode code="type" /> | `string` | The type of the resource. The value should always be archives. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_logs_archive" /> | `SELECT` | <CopyableCode code="archive_id, dd_site" /> | Get a specific archive from your organization. |
| <CopyableCode code="list_logs_archives" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the list of configured logs archives with their definitions. |
| <CopyableCode code="create_logs_archive" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create an archive in your organization. |
| <CopyableCode code="delete_logs_archive" /> | `DELETE` | <CopyableCode code="archive_id, dd_site" /> | Delete a given archive from your organization. |
| <CopyableCode code="_get_logs_archive" /> | `EXEC` | <CopyableCode code="archive_id, dd_site" /> | Get a specific archive from your organization. |
| <CopyableCode code="_list_logs_archives" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the list of configured logs archives with their definitions. |
| <CopyableCode code="add_read_role_to_archive" /> | `EXEC` | <CopyableCode code="archive_id, dd_site" /> | Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) |
| <CopyableCode code="remove_role_from_archive" /> | `EXEC` | <CopyableCode code="archive_id, dd_site" /> | Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) |
| <CopyableCode code="update_logs_archive" /> | `EXEC` | <CopyableCode code="archive_id, dd_site" /> | Update a given archive configuration.<br /><br />**Note**: Using this method updates your archive configuration by **replacing**<br />your current configuration with the new one sent to your Datadog organization. |
