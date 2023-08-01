---
title: nfs_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - nfs_shares
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>nfs_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.nfs_shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nfsShares` | `array` | The list of NFS shares. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token identifying a page of results from the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, nfsSharesId, projectsId` | Get details of a single NFS share. |
| `list` | `SELECT` | `locationsId, projectsId` | List NFS shares. |
| `create` | `INSERT` | `locationsId, projectsId` | Create an NFS share. |
| `delete` | `DELETE` | `locationsId, nfsSharesId, projectsId` | Delete an NFS share. The underlying volume is automatically deleted. |
| `patch` | `EXEC` | `locationsId, nfsSharesId, projectsId` | Update details of a single NFS share. |
| `rename` | `EXEC` | `locationsId, nfsSharesId, projectsId` | RenameNfsShare sets a new name for an nfsshare. Use with caution, previous names become immediately invalidated. |
