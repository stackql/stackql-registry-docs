---
title: advertiser_landing_pages
hide_title: false
hide_table_of_contents: false
keywords:
  - advertiser_landing_pages
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>advertiser_landing_pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.advertiser_landing_pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this landing page. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this landing page. This is a required field. It must be less than 256 characters long. |
| `url` | `string` | URL of this landing page. This is a required field. |
| `advertiserId` | `string` | Advertiser ID of this landing page. This is a required field. |
| `archived` | `boolean` | Whether this landing page has been archived. |
| `deepLinks` | `array` | Links that will direct the user to a mobile app, if installed. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#landingPage". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertiserLandingPages_get` | `SELECT` | `id, profileId` | Gets one landing page by ID. |
| `advertiserLandingPages_list` | `SELECT` | `profileId` | Retrieves a list of landing pages. |
| `advertiserLandingPages_insert` | `EXEC` | `profileId` | Inserts a new landing page. |
| `advertiserLandingPages_patch` | `EXEC` | `id, profileId` | Updates an existing advertiser landing page. This method supports patch semantics. |
| `advertiserLandingPages_update` | `EXEC` | `profileId` | Updates an existing landing page. |
