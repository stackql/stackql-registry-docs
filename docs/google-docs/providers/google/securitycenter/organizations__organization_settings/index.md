---
title: organizations__organization_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations__organization_settings
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>organizations__organization_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.organizations__organization_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The relative resource name of the settings. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/&#123;organization_id&#125;/organizationSettings". |
| `enableAssetDiscovery` | `boolean` | A flag that indicates if Asset Discovery should be enabled. If the flag is set to `true`, then discovery of assets will occur. If it is set to `false, all historical assets will remain, but discovery of future assets will not occur. |
| `assetDiscoveryConfig` | `object` | The configuration used for Asset Discovery runs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_getOrganizationSettings` | `SELECT` | `organizationsId` |
