---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
  - datamigration
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
<tr><td><b>Name</b></td><td><code>connection_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.connection_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `connectionProfiles` | `array` | The response list of connection profiles. |
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionProfilesId, locationsId, projectsId` | Gets details of a single connection profile. |
| `list` | `SELECT` | `locationsId, projectsId` | Retrieves a list of all connection profiles in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new connection profile in a given project and location. |
| `delete` | `DELETE` | `connectionProfilesId, locationsId, projectsId` | Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs. |
| `patch` | `EXEC` | `connectionProfilesId, locationsId, projectsId` | Update the configuration of a single connection profile. |
