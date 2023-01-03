---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - connectors
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Version. Format: projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version} |
| `configVariableTemplates` | `array` | Output only. List of config variables needed to create a connection. |
| `createTime` | `string` | Output only. Created time. |
| `authConfigTemplates` | `array` | Output only. List of auth configs supported by the Connector Version. |
| `releaseVersion` | `string` | Output only. ReleaseVersion of the connector, for example: "1.0.1-alpha". |
| `updateTime` | `string` | Output only. Updated time. |
| `labels` | `object` | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `launchStage` | `string` | Output only. Flag to mark the version indicating the launch stage. |
| `egressControlConfig` | `object` | Egress control config for connector runtime. These configurations define the rules to identify which outbound domains/hosts needs to be whitelisted. It may be a static information for a particular connector version or it is derived from the configurations provided by the customer in Connection resource. |
| `roleGrant` | `object` | This configuration defines all the Cloud IAM roles that needs to be granted to a particular GCP resource for the selected prinicpal like service account. These configurations will let UI display to customers what IAM roles need to be granted by them. Or these configurations can be used by the UI to render a 'grant' button to do the same on behalf of the user. |
| `roleGrants` | `array` | Output only. Role grant configurations for this connector version. |
| `supportedRuntimeFeatures` | `object` | Supported runtime features of a connector version. This is passed to the management layer to add a new connector version by the connector developer. Details about how this proto is passed to the management layer is covered in this doc - go/runtime-manifest. |
| `displayName` | `string` | Output only. Display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_providers_connectors_versions_get` | `SELECT` | `connectorsId, projectsId, providersId, versionsId` | Gets details of a single connector version. |
| `projects_locations_global_providers_connectors_versions_list` | `SELECT` | `connectorsId, projectsId, providersId` | Lists Connector Versions in a given project and location. |
