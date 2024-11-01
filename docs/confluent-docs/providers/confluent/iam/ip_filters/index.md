---
title: ip_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_filters
  - iam
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.ip_filters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="filter_name" /> | `string` | A human readable name for an IP Filter. Can contain any unicode letter or number, the ASCII space character,<br />or any of the following special characters: `[`, `]`, `\|`, `&`, `+`, `-`, `_`, `/`, `.`, `,`.<br /> |
| <CopyableCode code="ip_groups" /> | `array` | A list of IP Groups. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="resource_group" /> | `string` | Scope of resources covered by this IP filter. The only resource_group currently available is "management".<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2ip_filter" /> | `SELECT` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to read an IP filter. |
| <CopyableCode code="list_iam_v2ip_filters" /> | `SELECT` |  | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Retrieve a sorted, filtered, paginated list of all IP filters. |
| <CopyableCode code="create_iam_v2ip_filter" /> | `INSERT` |  | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to create an IP filter. |
| <CopyableCode code="delete_iam_v2ip_filter" /> | `DELETE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to delete an IP filter. |
| <CopyableCode code="update_iam_v2ip_filter" /> | `UPDATE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to update an IP filter.<br /><br /> |
