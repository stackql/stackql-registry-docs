---
title: targeting_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - targeting_templates
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
<tr><td><b>Name</b></td><td><code>targeting_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.targeting_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this targeting template. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this targeting template. This field is required. It must be less than 256 characters long and unique within an advertiser. |
| `subaccountId` | `string` | Subaccount ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `keyValueTargetingExpression` | `object` | Key Value Targeting Expression. |
| `accountId` | `string` | Account ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert. |
| `advertiserId` | `string` | Advertiser ID of this targeting template. This is a required field on insert and is read-only after insert. |
| `technologyTargeting` | `object` | Technology Targeting. |
| `listTargetingExpression` | `object` | Remarketing List Targeting Expression. |
| `dayPartTargeting` | `object` | Day Part Targeting. |
| `geoTargeting` | `object` | Geographical Targeting. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#targetingTemplate". |
| `languageTargeting` | `object` | Language Targeting. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetingTemplates_get` | `SELECT` | `id, profileId` | Gets one targeting template by ID. |
| `targetingTemplates_list` | `SELECT` | `profileId` | Retrieves a list of targeting templates, optionally filtered. This method supports paging. |
| `targetingTemplates_insert` | `EXEC` | `profileId` | Inserts a new targeting template. |
| `targetingTemplates_patch` | `EXEC` | `id, profileId` | Updates an existing targeting template. This method supports patch semantics. |
| `targetingTemplates_update` | `EXEC` | `profileId` | Updates an existing targeting template. |
