---
title: conformance_packs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - conformance_packs_list_only
  - config
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

Lists <code>conformance_packs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/conformance_packs/"><code>conformance_packs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_packs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.conformance_packs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="conformance_pack_name" /></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="delivery_s3_bucket" /></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><CopyableCode code="delivery_s3_key_prefix" /></td><td><code>string</code></td><td>The prefix for delivery S3 bucket.</td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td>A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><CopyableCode code="template_s3_uri" /></td><td><code>string</code></td><td>Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><CopyableCode code="template_ssm_document_details" /></td><td><code>object</code></td><td>The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.</td></tr>
<tr><td><CopyableCode code="conformance_pack_input_parameters" /></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
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
Lists all <code>conformance_packs</code> in a region.
```sql
SELECT
region,
conformance_pack_name
FROM aws.config.conformance_packs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>conformance_packs_list_only</code> resource, see <a href="/providers/aws/config/conformance_packs/#permissions"><code>conformance_packs</code></a>


