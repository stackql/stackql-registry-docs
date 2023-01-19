---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - adsense
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of a site. Format: accounts/&#123;account&#125;/sites/&#123;site&#125; |
| `domain` | `string` | Domain (or subdomain) of the site, e.g. "example.com" or "www.example.com". This is used in the `OWNED_SITE_DOMAIN_NAME` reporting dimension. |
| `reportingDimensionId` | `string` | Output only. Unique ID of the site as used in the `OWNED_SITE_ID` reporting dimension. |
| `state` | `string` | Output only. State of a site. |
| `autoAdsEnabled` | `boolean` | Whether auto ads is turned on for the site. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_sites_get` | `SELECT` | `accountsId, sitesId` | Gets information about the selected site. |
| `accounts_sites_list` | `SELECT` | `accountsId` | Lists all the sites available in an account. |
