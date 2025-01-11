---
title: crawler_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - crawler_tags
  - glue
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

Expands all tag keys and values for <code>crawlers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crawler_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Crawler</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.crawler_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="classifiers" /></td><td><code>array</code></td><td>A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the crawler.</td></tr>
<tr><td><CopyableCode code="schema_change_policy" /></td><td><code>object</code></td><td>The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The SchemaChangePolicy does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the SchemaChangePolicy on a crawler. The SchemaChangePolicy consists of two components, UpdateBehavior and DeleteBehavior.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>string</code></td><td>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior.</td></tr>
<tr><td><CopyableCode code="recrawl_policy" /></td><td><code>object</code></td><td>When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. For more information, see Incremental Crawls in AWS Glue in the developer guide.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of the database in which the crawler's output is stored.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>object</code></td><td>Specifies data stores to crawl.</td></tr>
<tr><td><CopyableCode code="crawler_security_configuration" /></td><td><code>string</code></td><td>The name of the SecurityConfiguration structure to be used by this crawler.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the crawler.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.</td></tr>
<tr><td><CopyableCode code="lake_formation_configuration" /></td><td><code>object</code></td><td>Specifies AWS Lake Formation configuration settings for the crawler</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>A scheduling object using a cron statement to schedule an event.</td></tr>
<tr><td><CopyableCode code="table_prefix" /></td><td><code>string</code></td><td>The prefix added to the names of tables that are created.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>crawlers</code> in a region.
```sql
SELECT
region,
classifiers,
description,
schema_change_policy,
configuration,
recrawl_policy,
database_name,
targets,
crawler_security_configuration,
name,
role,
lake_formation_configuration,
schedule,
table_prefix,
tag_key,
tag_value
FROM aws.glue.crawler_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>crawler_tags</code> resource, see <a href="/providers/aws/glue/crawlers/#permissions"><code>crawlers</code></a>

