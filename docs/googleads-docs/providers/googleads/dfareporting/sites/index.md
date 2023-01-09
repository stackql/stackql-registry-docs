---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this site. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this site.This is a required field. Must be less than 128 characters long. If this site is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this site is a top-level site, and the name must be unique among top-level sites of the same account. |
| `accountId` | `string` | Account ID of this site. This is a read-only field that can be left blank. |
| `siteContacts` | `array` | Site contacts. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#site". |
| `videoSettings` | `object` | Video Settings |
| `approved` | `boolean` | Whether this site is approved. |
| `subaccountId` | `string` | Subaccount ID of this site. This is a read-only field that can be left blank. |
| `siteSettings` | `object` | Site Settings |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `directorySiteIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `directorySiteId` | `string` | Directory site associated with this site. This is a required field that is read-only after insertion. |
| `keyName` | `string` | Key name of this site. This is a read-only, auto-generated field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one site by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of sites, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new site. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing site. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing site. |
