---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `instances` | `array` | The list of servers. |
| `nextPageToken` | `string` | A token identifying a page of results from the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Get details about a single server. |
| `list` | `SELECT` | `locationsId, projectsId` | List servers in a given project and location. |
| `detach_lun` | `EXEC` | `instancesId, locationsId, projectsId` | Detach LUN from Instance. |
| `disable_interactive_serial_console` | `EXEC` | `instancesId, locationsId, projectsId` | Disable the interactive serial console feature on an instance. |
| `enable_interactive_serial_console` | `EXEC` | `instancesId, locationsId, projectsId` | Enable the interactive serial console feature on an instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Update details of a single server. |
| `rename` | `EXEC` | `instancesId, locationsId, projectsId` | RenameInstance sets a new name for an instance. Use with caution, previous names become immediately invalidated. |
| `reset` | `EXEC` | `instancesId, locationsId, projectsId` | Perform an ungraceful, hard reset on a server. Equivalent to shutting the power off and then turning it back on. |
| `start` | `EXEC` | `instancesId, locationsId, projectsId` | Starts a server that was shutdown. |
| `stop` | `EXEC` | `instancesId, locationsId, projectsId` | Stop a running server. |
