---
title: vendors
hide_title: false
hide_table_of_contents: false
keywords:
  - vendors
  - vendors
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vendors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.vendors.vendors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The short name of the vendor |
| `description` | `string` | A short description of this vendor, and common use-cases of integrations for this vendor. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `integration_guide_url` | `string` | URL of an integration guide for this vendor |
| `logo_url` | `string` | URL of a logo identifying the vendor |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `thumbnail_url` | `string` | URL of a small thumbnail image identifying the vendor |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `website_url` | `string` | URL of the vendor's main website |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_vendor` | `SELECT` | `id` | Get details about one specific vendor.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| `list_vendors` | `SELECT` |  | List all vendors.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| `_get_vendor` | `EXEC` | `id` | Get details about one specific vendor.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| `_list_vendors` | `EXEC` |  | List all vendors.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
