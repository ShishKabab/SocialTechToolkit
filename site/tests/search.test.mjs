import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {search,validateIndex,normalize,distance} from '../assets/search-core.js';
const index=validateIndex(JSON.parse(fs.readFileSync(new URL('../dist/search-index.json',import.meta.url))));
test('exact titles take precedence over fuzzy neighboring concepts',()=>{assert.equal(search(index,'consent')[0].title,'Consent decision-making');assert.equal(search(index,'Consensus process')[0].title,'Consensus process');});
test('aliases, word order, accents, and punctuation normalize',()=>{assert.equal(search(index,'BDFL')[0].title,'BDFL governance');assert.equal(search(index,'worker co-ops')[0].title,'Worker cooperatives');assert.equal(search(index,'talks lightning')[0].title,'Recurring open gatherings');assert.equal(normalize('Café—WORLD'),'cafe world');});
test('transposed letters and spelling errors match longer terms',()=>{assert.equal(distance('ligthning','lightning'),1);assert.equal(search(index,'consnesus process')[0].title,'Consensus process');assert.equal(search(index,'apprentceship')[0].title,'Apprenticeship');});
test('curated discovery terms find multiple related entries',()=>{assert.equal(search(index,'short presentations')[0].title,'Recurring open gatherings');const names=search(index,'shared ownership').map(e=>e.title);assert(names.includes('Worker cooperatives'));assert(names.includes('Housing cooperatives'));});
test('all query words must match, short terms do not fuzzy expand',()=>{assert.deepEqual(search(index,'lightning spaceship'),[]);assert.equal(search(index,'bdf')[0].title,'BDFL governance');assert.equal(search(index,'bxf').length,0);assert.equal(search(index,'xyzqpk').length,0);assert.equal(search(index,'   ').length,0);});
test('invalid indexes and duplicate IDs fail closed',()=>{assert.throws(()=>validateIndex({}));assert.throws(()=>validateIndex([]));assert.throws(()=>validateIndex([index[0],index[0]]));assert.throws(()=>validateIndex([{...index[0],url:'//evil.example'}]));assert.throws(()=>validateIndex([{...index[0],aliases:[123]}]));});

test('mentorship typo and alias find the mentorship entry',()=>{assert.equal(search(index,'mentroship')[0].title,'Mentorship');assert.equal(search(index,'mentoring')[0].title,'Mentorship');});

test('consolidated components lead to their explanation without becoming aliases',()=>{for(const [query,title] of [['community monitoring','Commons governance'],['leadership pipelines','Succession planning'],['peer nominations','Awards'],['deliberate practice','Apprenticeship']]){const result=search(index,query)[0];assert.equal(result.title,title);assert.match(result.explanation,/^Related to /);}});
