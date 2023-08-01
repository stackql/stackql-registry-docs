---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - notebooks
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
<tr><td><b>Id</b></td><td><code>google.notebooks.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Page token that can be used to continue listing from the last result in the next list call. |
| `unreachable` | `array` | Locations that could not be reached. For example, ['us-west1-a', 'us-central1-b']. A ListInstancesResponse will only contain either instances or unreachables, |
| `instances` | `array` | A list of returned instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists instances in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given project and location. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `check_upgradability` | `EXEC` | `instancesId, locationsId, projectsId` | Checks whether a notebook instance is upgradable. |
| `diagnose` | `EXEC` | `instancesId, locationsId, projectsId` | Creates a Diagnostic File and runs Diagnostic Tool given an Instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | UpdateInstance updates an Instance. |
| `report_info_system` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly. |
| `reset` | `EXEC` | `instancesId, locationsId, projectsId` | Resets a notebook instance. |
| `rollback` | `EXEC` | `instancesId, locationsId, projectsId` | Rollbacks a notebook instance to the previous version. |
| `start` | `EXEC` | `instancesId, locationsId, projectsId` | Starts a notebook instance. |
| `stop` | `EXEC` | `instancesId, locationsId, projectsId` | Stops a notebook instance. |
| `upgrade` | `EXEC` | `instancesId, locationsId, projectsId` | Upgrades a notebook instance to the latest version. |
| `upgrade_system` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to upgrade themselves. Do not use this method directly. |
