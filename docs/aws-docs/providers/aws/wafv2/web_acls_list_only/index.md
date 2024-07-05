---
title: web_acls_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - web_acls_list_only
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>web_acls</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/web_acls/"><code>web_acls</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_acls_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.web_acls_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="default_action" /></td><td><code>object</code></td><td>Default Action WebACL will take against ingress traffic when there is no matching Rule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the entity.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the WebACL.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the WebACL</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront WebACL, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><CopyableCode code="visibility_config" /></td><td><code>object</code></td><td>Visibility Metric of the WebACL.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="label_namespace" /></td><td><code>string</code></td><td>Name of the Label.</td></tr>
<tr><td><CopyableCode code="custom_response_bodies" /></td><td><code>object</code></td><td>Custom response key and body map.</td></tr>
<tr><td><CopyableCode code="captcha_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="challenge_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="token_domains" /></td><td><code>array</code></td><td>List of domains to accept in web request tokens, in addition to the domain of the protected resource.</td></tr>
<tr><td><CopyableCode code="association_config" /></td><td><code>object</code></td><td>AssociationConfig for body inspection</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>web_acls</code> in a region.
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.web_acls_list_only
;
```


## Permissions

For permissions required to operate on the <code>web_acls_list_only</code> resource, see <a href="/providers/aws/wafv2/web_acls/#permissions"><code>web_acls</code></a>


