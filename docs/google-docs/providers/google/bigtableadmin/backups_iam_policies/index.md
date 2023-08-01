---
title: backups_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_iam_policies
  - bigtableadmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.backups_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_iam_policy` | `EXEC` | `backupsId, clustersId, instancesId, projectsId` | Gets the access control policy for a Table resource. Returns an empty policy if the resource exists but does not have a policy set. |
| `set_iam_policy` | `EXEC` | `backupsId, clustersId, instancesId, projectsId` | Sets the access control policy on a Table resource. Replaces any existing policy. |
| `test_iam_permissions` | `EXEC` | `backupsId, clustersId, instancesId, projectsId` | Returns permissions that the caller has on the specified table resource. |
