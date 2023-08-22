---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
  - datastream
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
<tr><td><b>Id</b></td><td><code>google.datastream.connection_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource's name. |
| `updateTime` | `string` | Output only. The update time of the resource. |
| `labels` | `object` | Labels. |
| `createTime` | `string` | Output only. The create time of the resource. |
| `gcsProfile` | `object` | Cloud Storage bucket profile. |
| `postgresqlProfile` | `object` | PostgreSQL database profile. |
| `displayName` | `string` | Required. Display name. |
| `privateConnectivity` | `object` | Private Connectivity |
| `staticServiceIpConnectivity` | `object` | Static IP address connectivity. Used when the source database is configured to allow incoming connections from the Datastream public IP addresses for the region specified in the connection profile. |
| `oracleProfile` | `object` | Oracle database profile. |
| `mysqlProfile` | `object` | MySQL database profile. |
| `bigqueryProfile` | `object` | BigQuery warehouse profile. |
| `forwardSshConnectivity` | `object` | Forward SSH Tunnel connectivity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionProfilesId, locationsId, projectsId` | Use this method to get details about a connection profile. |
| `list` | `SELECT` | `locationsId, projectsId` | Use this method to list connection profiles created in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Use this method to create a connection profile in a project and location. |
| `delete` | `DELETE` | `connectionProfilesId, locationsId, projectsId` | Use this method to delete a connection profile. |
| `_list` | `EXEC` | `locationsId, projectsId` | Use this method to list connection profiles created in a project and location. |
| `discover` | `EXEC` | `locationsId, projectsId` | Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request. |
| `patch` | `EXEC` | `connectionProfilesId, locationsId, projectsId` | Use this method to update the parameters of a connection profile. |
