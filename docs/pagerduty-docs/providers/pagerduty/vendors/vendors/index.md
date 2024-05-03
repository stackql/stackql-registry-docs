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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vendors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.vendors.vendors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The short name of the vendor |
| <CopyableCode code="description" /> | `string` | A short description of this vendor, and common use-cases of integrations for this vendor. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="integration_guide_url" /> | `string` | URL of an integration guide for this vendor |
| <CopyableCode code="logo_url" /> | `string` | URL of a logo identifying the vendor |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="thumbnail_url" /> | `string` | URL of a small thumbnail image identifying the vendor |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="website_url" /> | `string` | URL of the vendor's main website |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_vendor" /> | `SELECT` | <CopyableCode code="id" /> | Get details about one specific vendor.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| <CopyableCode code="list_vendors" /> | `SELECT` |  | List all vendors.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| <CopyableCode code="_get_vendor" /> | `EXEC` | <CopyableCode code="id" /> | Get details about one specific vendor.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
| <CopyableCode code="_list_vendors" /> | `EXEC` |  | List all vendors.<br /><br />A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#vendors)<br /><br />Scoped OAuth requires: `vendors.read`<br /> |
