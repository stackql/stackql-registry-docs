---
title: authentication_config
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_config
  - contactcenteraiplatform
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
<tr><td><b>Name</b></td><td><code>authentication_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenteraiplatform.authentication_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of authentication config. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/contactCenters/&#123;contact_center&#125;/authentication-config |
| `samlSetting` | `object` |  |
| `basicAuthSetting` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_authentication-config` | `SELECT` | `contactCentersId, locationsId, projectsId` |
| `update_authentication-config` | `EXEC` | `contactCentersId, locationsId, projectsId` |
