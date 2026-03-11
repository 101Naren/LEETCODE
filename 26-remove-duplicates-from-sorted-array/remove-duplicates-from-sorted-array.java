class Solution {
    public int removeDuplicates(int[] nums) {
        LinkedHashMap<Integer,Integer>map = new LinkedHashMap<>();
        ArrayList<Integer>list=new ArrayList<>();
        for(int i = 0; i<nums.length;i++)
        {
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        for(int x:map.keySet())
        {
            list.add(x);
        }
        for(int i = 0;i<list.size();i++)
        {
            nums[i]=list.get(i);
        }
        return list.size();
    }
}